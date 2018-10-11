import os

import yaml
from exception.exception import ConfigDoesNotExist
from context_manager.manager import manager


def parse(dir, name):
    path = os.path.join(dir, name)
    with manager(path, 'r', ConfigDoesNotExist(path)) as stream:
        config = yaml.load(stream)

    return config['token'], config['backend'], config['db'], config['dialog'], config['filename']
