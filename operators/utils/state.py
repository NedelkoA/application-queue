import json


def change_state(obj, target):
    with open('operators/configs/state_config.json', 'r') as f:
        conf = json.load(f)
    obj_status = obj.status
    if obj_status in conf:
        current_status = conf.get(obj_status)
        if target in current_status:
            obj.status = target
            return obj

