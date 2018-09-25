import json

import pika

from queue.backends.base import BaseQueueWrapper
# from settings import QUEUE_SERVER


class RabbitmqQueue(BaseQueueWrapper):
    name = 'rabbitmq'

    def get_conn_params(self):
        conn_params = {}
        if self.settings_dict['HOST']:
            conn_params['host'] = self.settings_dict['HOST']
        if self.settings_dict['PORT']:
            conn_params['port'] = self.settings_dict['PORT']
        return conn_params

    def new_connection(self, connection_params):
        return pika.BlockingConnection(pika.ConnectionParameters(
            **connection_params
        ))

    def push(self, **data):
        channel = self.connection.channel()
        channel.queue_declare(queue='item_list')
        channel.basic_publish(
            exchange='',
            routing_key='item_list',
            body=json.dumps(data)
        )

    def pop(self):
        channel = self.connection.channel()
        item = channel.basic_get(
            queue='item_list',
            no_ack=True
        )
        if item[2]:
            return json.loads(item[2].decode('utf-8'))


# r = RabbitmqQueue(QUEUE_SERVER)
# da = {
#     'asd': 'hello',
#     'some': 'good bye'
# }
# da_2 = {
#     'asd': 'hello1',
#     'some': 'good bye1'
# }
# r.connect()
# print(r.connection)
# r.push(**da)
# r.push(**da_2)
# print(r.pop())
# print(r.pop())
# r.connection.close()
