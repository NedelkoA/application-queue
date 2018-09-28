from importlib import import_module
from django.conf import settings


def _get_queue(queue_data):
    if queue_data['ENGINE']:
        engine = queue_data['ENGINE'].rsplit('.', 1)
        queue_module = import_module(engine[0])
        queue = getattr(queue_module, engine[1])
        return queue


def get_connection():
    queue = _get_queue(settings.QUEUE_SERVER)(settings.QUEUE_SERVER)
    queue.connect()
    return queue
