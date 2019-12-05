from database import SQLite

import uuid

def get_id():
    return str(uuid.uuid1())


class Post(object):

    def __init__(self, post_id, title, content):
        self.id = post_id
        self.title = title
        self.content = content

    def to_dict(self):
        return self.__dict__

    def save(self):
        with SQLite() as db:
            db.execute(
                    "INSERT INTO  post (id, title, content) VALUES (?, ?, ?)",
                    (self.id, self.title, self.content))
        return self

    @staticmethod
    def find(post_id):
        with SQLite() as db:
            result = db.execute(
                    "SELECT id, title, content FROM post WHERE id = ?",
                    (post_id,)).fetchone()
            return Post(*result)

    @staticmethod
    def all():
        with SQLite() as db:
            result = db.execute(
                    "SELECT id, title, content FROM post").fetchall()
            return [Post(*row) for row in result]

