from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, aliased
from sqlalchemy.sql.expression import func
    
from database import Base

class UserLike(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    liked_by = Column(Integer, ForeignKey("users.id"), index=True)
    liked_user = Column(Integer, ForeignKey("users.id"))

    @staticmethod
    def find_matches(current_user):
        aliased_likes = aliased(UserLike)
        matches = UserLike.query.filter(UserLike.liked_by == current_user.id). \
                join(aliased_likes,
                        UserLike.liked_user == aliased_likes.liked_by).all()
        return [UserLike.__find_users(match) for match in matches]

    @staticmethod
    def __find_users(match):
        liked_by = User.query.filter_by(id=match.liked_by).first()
        liked = User.query.filter_by(id=match.liked_user).first()
        return (liked_by, liked)

    def __repr__(self):
        return '<UserLike ({}, {}, {})>'.format(self.id, self.liked_by, self.liked_user)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    login_id = Column(String(36), nullable=True)
    first_name = Column(String(120), unique=False, nullable=True) 
    last_name = Column(String(120), unique=False, nullable=True) 
    age = Column(Integer(), unique=False, nullable=True) 
    bio = Column(String(512), unique=False, nullable=True)
    profile_pic = Column(String(120), unique=False, nullable=True)

    likes = relationship("UserLike", foreign_keys=[UserLike.liked_by])

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @staticmethod
    def find_another_random(user):
        liked_user_ids = [like.liked_user for like in user.likes]
        return User.query.filter(User.id != user.id,
                User.id.notin_(liked_user_ids)).first()

    def get_id(self):
        return self.login_id

    def __repr__(self):
        return '<User %r>' % self.username
