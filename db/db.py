class Db:
    def __init__(self, db):
        self.db = db

    def hget(self, id, key):
        return self.db.hget(id, key)

    def hset(self, id, key, value):
        return self.db.hset(id, key, value)

    def save_image(self, id, key, filename):
        img = open(filename, "rb")
        self.db.hset(id, key, img.read())
        img.close()
