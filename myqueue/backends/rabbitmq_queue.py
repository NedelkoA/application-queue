import json
from collections import namedtuple

import pika

from myqueue.backends.base import BaseQueueWrapper

Item = namedtuple('Item', [
            'channel',
            'properties',
            'data'
        ])


class RabbitmqQueue(BaseQueueWrapper):
    name = 'rabbitmq'

    def get_conn_params(self):
        conn_params = {}
        if self.settings_dict['HOST']:
            conn_params['host'] = self.settings_dict['HOST']
        if self.settings_dict['PORT']:
            conn_params['port'] = self.settings_dict['PORT']
        if not self.settings_dict['QUEUE_NAME']:
            raise ValueError('QUEUE_NAME is required!')
        return conn_params

    def new_connection(self, connection_params):
        return pika.BlockingConnection(pika.ConnectionParameters(
            **connection_params
        ))

    def push(self, **data):
        channel = self.connection.channel()
        channel.queue_declare(queue=self.settings_dict['QUEUE_NAME'])
        channel.basic_publish(
            exchange='',
            routing_key=self.settings_dict['QUEUE_NAME'],
            body=json.dumps(data)
        )

    def pop(self):
        channel = self.connection.channel()
        queue_item = channel.basic_get(
            queue=self.settings_dict['QUEUE_NAME'],
            no_ack=True
        )
        item = Item(*queue_item)
        if item.data:
            return json.loads(item.data.decode('utf-8'))

    @property
    def count_items(self):
        channel = self.connection.channel()
        rabbit_queue = channel.queue_declare(queue=self.settings_dict['QUEUE_NAME'])
        return rabbit_queue.method.message_count
