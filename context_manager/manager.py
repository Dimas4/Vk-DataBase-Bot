from contextlib import contextmanager


@contextmanager
def manager(path, mode, Exception):
    try:
        file = open(path, mode)
    except FileNotFoundError:
        raise Exception

    yield file

    file.close()
