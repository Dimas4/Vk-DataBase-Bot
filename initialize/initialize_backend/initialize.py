import importlib


def initialize(token, backend):
    module = importlib.import_module(backend, ".")
    return module.VkBot(token)
