from redis import StrictRedis


class Db:
    def __init__(self, host='localhost', port=6379, db_c=0):
        self.host = host
        self.port = port
        self.db_c = db_c
        self.db = StrictRedis(host='localhost', port=6379, db=0)

    def hget(self, id, key):
        return self.db.hget(id, key)

    def hset(self, id, key, value):
        return self.db.hset(id, key, value)
