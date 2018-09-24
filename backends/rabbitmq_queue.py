import pika

from backends.base import BaseQueueWrapper
from settings import QUEUE_SERVER


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


r = RabbitmqQueue(QUEUE_SERVER)

r.connect()
print(r.connection)
r.connection.close()
