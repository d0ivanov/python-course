import hashlib

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from database import DB

SECRET = 'bFH6!CtTg2ggR632TvNSZZ*oPPvbeK*p@DspAACPpD'

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


    def create(self):
        with DB() as db:
            values = (self.username, self.password)
            db.execute('''
                INSERT INTO users (username, password)
                VALUES (?, ?)''', values)
            return self


    @staticmethod
    def find_by_username(username):
        if not username:
            return None
        with DB() as db:
            row = db.execute(
                'SELECT * FROM users WHERE username = ?',
                (username,)
            ).fetchone()
            if row:
                return User(*row)


    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()


    def verify_password(self, password):
        return self.password == hashlib.sha256(password.encode('utf-8')).hexdigest()

    def generate_auth_token(self, expiration=600):
        s = Serializer(SECRET, expires_in=expiration)
        return s.dumps({'username': self.username})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        return True

