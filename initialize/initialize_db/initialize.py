import importlib


def initialize(path, **kwargs):
    module = importlib.import_module(path, ".")
    return module.Db(kwargs)
