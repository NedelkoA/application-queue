class BaseQueueWrapper:
    name = None

    def __init__(self, settings_dict):
        self.settings_dict = settings_dict
        self.connection = None

    def get_conn_params(self):
        raise NotImplementedError('subclasses of BaseQueueWrapper may require a get_conn_params() method')

    def new_connection(self, connection_params):
        raise NotImplementedError('subclasses of BaseQueueWrapper may require a new_connection() method')

    def connect(self):
        conn_params = self.get_conn_params()
        self.connection = self.new_connection(conn_params)

    def push(self, **data):
        raise NotImplementedError('subclasses of BaseQueueWrapper may require a push() method')

    def pop(self):
        raise NotImplementedError('subclasses of BaseQueueWrapper may require a pop() method')