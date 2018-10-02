from abc import ABCMeta, abstractmethod, abstractproperty


class BaseQueueWrapper(metaclass=ABCMeta):
    def __init__(self, settings_dict):
        self.settings_dict = settings_dict
        self.connection = None

    @abstractmethod
    def get_conn_params(self):
        pass

    @abstractmethod
    def new_connection(self, connection_params):
        pass

    def connect(self):
        conn_params = self.get_conn_params()
        self.connection = self.new_connection(conn_params)

    @abstractmethod
    def push(self, **data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractproperty
    def count_items(self):
        pass
