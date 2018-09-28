import json

import redis

from myqueue.backends.base import BaseQueueWrapper


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
        return redis.Redis(**connection_params, decode_responses=True)

    def push(self, **data):
        self.connection.rpush('item_list', json.dumps(data))

    def pop(self):
        data = self.connection.lpop('item_list')
        if data:
            return json.loads(data)


# r = RedisQueue(QUEUE_SERVER)
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