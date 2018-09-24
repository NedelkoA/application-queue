import redis

from backends.base import BaseQueueWrapper
from settings import QUEUE_SERVER


class RedisQueue(BaseQueueWrapper):
    name = 'redis'

    def get_conn_params(self):
        conn_params = {}
        if self.settings_dict['HOST']:
            conn_params['host'] = self.settings_dict['HOST']
        if self.settings_dict['PORT']:
            conn_params['port'] = self.settings_dict['PORT']
        if self.settings_dict['DB']:
            conn_params['db'] = self.settings_dict['DB']
        return conn_params

    def new_connection(self, connection_params):
        return redis.Redis(**connection_params)


r = RedisQueue(QUEUE_SERVER)

r.connect()
print(r.connection)
