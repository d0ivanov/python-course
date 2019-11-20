from database import DB

class Post:
    def __init__(self, id, name, author, content):
        self.id = id
        self.name = name
        self.author = author
        self.content = content

    @staticmethod
    def all():
        with DB() as db:
            rows = db.execute('SELECT * FROM posts').fetchall()
            return [Post(*row) for row in rows]

    @staticmethod
    def find(id):
        with DB() as db:
            row = db.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()
            return Post(*row)

    def create(self):
        with DB() as db:
            values = (self.name, self.author, self.content)
            row = db.execute('INSERT INTO posts (name, author, content) VALUES (?, ?, ?)', values)
            return self
