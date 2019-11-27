from database import DB


class Comment:
    def __init__(self, id, post, message):
        self.id = id
        self.post = post
        self.message = message

    def create(self):
        with DB() as db:
            values = (self.post.id, self.message)
            db.execute(
                'INSERT INTO comments (post_id, message) VALUES (?, ?)',
                values
            )
            return self

    @staticmethod
    def find_by_post(post):
        with DB() as db:
            rows = db.execute(
                'SELECT * FROM comments WHERE post_id = ?',
                (post.id,)
            ).fetchall()
            return [Comment(*row) for row in rows]
