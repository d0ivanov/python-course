from database import DB
from comment import Comment


class Post:
    def __init__(self, id, name, author, content, category):
        self.id = id
        self.name = name
        self.author = author
        self.content = content
        self.category = category

    @staticmethod
    def all():
        with DB() as db:
            rows = db.execute('SELECT * FROM posts').fetchall()
            return [Post(*row) for row in rows]

    @staticmethod
    def find(id):
        with DB() as db:
            row = db.execute(
                'SELECT * FROM posts WHERE id = ?',
                (id,)
            ).fetchone()
            return Post(*row)

    @staticmethod
    def find_by_category(category):
        with DB() as db:
            rows = db.execute(
                'SELECT * FROM posts WHERE category_id = ?',
                (category.id,)
            ).fetchall()
            return [Post(*row) for row in rows]

    def create(self):
        with DB() as db:
            values = (self.name, self.author, self.content, self.category.id)
            db.execute('''
                INSERT INTO posts (name, author, content, category_id)
                VALUES (?, ?, ?, ?)''', values)
            return self

    def save(self):
        with DB() as db:
            values = (
                self.name,
                self.author,
                self.content,
                self.category.id,
                self.id
            )
            db.execute(
                '''UPDATE posts
                SET name = ?, author = ?, content = ?, category_id = ?
                WHERE id = ?''', values)
            return self

    def delete(self):
        with DB() as db:
            db.execute('DELETE FROM posts WHERE id = ?', (self.id,))

    def comments(self):
        return Comment.find_by_post(self)
