from flask import Flask
from flask import render_template, request, flash, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from functools import wraps
from itsdangerous import (
        TimedJSONWebSignatureSerializer as Serializer,
        BadSignature,
        SignatureExpired
        )

import hashlib
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dev.db'
app.secret_key = "eusehuccuhosn23981pcgid1xth4dn"

db = SQLAlchemy(app)

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_token(token):
    s = Serializer(app.secret_key)
    try:
        s.loads(token)
    except SignatureExpired:
        return False
    except BadSignature:
        return False
    return True

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        if not token or not verify_token(token):
            flash('You have to be logged in to access this page')
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper

def stop_logged_users(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        if token and verify_token(token):
            flash('You\'re already logged in.')
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper

likes_table = db.Table('like', db.Model.metadata,
        db.Column('liking_user_id', db.Integer, db.ForeignKey('user.id'), index=True),
        db.Column('liked_user_id', db.Integer, db.ForeignKey('user.id')))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    likes = db.relationship(
            'User',
            secondary=likes_table,
            primaryjoin=id==likes_table.c.liking_user_id,
            secondaryjoin=id==likes_table.c.liked_user_id,
            backref='liked_by'
            )

    def __init__(self, **kwargs):
        if 'password' in kwargs:
            kwargs['password'] = hash_password(kwargs['password'])
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.username

    def verify_password(self, password):
        return self.password == hash_password(password)

    def generate_token(self):
        s = Serializer(app.secret_key, expires_in=600)
        return s.dumps({'username': self.username})

    @staticmethod
    def find_by_token(token):
        if not token:
            return None

        try:
            s = Serializer(app.secret_key)
            payload = s.loads(token)
            return User.query.filter_by(username=payload.get('username')).first()
        except SignatureExpired:
            return None


@app.route('/')
@require_login
def index():
    token = request.cookies.get('token')
    current_user = User.find_by_token(token)
    random_user = User.query.filter(User.id != current_user.id).order_by(func.random()).first()
    i = 0
    users_count = User.query.count()
    while random_user in current_user.likes:
        i += 1
        if i >= users_count:
            random_user = None
            break
        random_user = User.query.filter(User.id != current_user.id).order_by(func.random()).first()
    print(current_user.likes)
    print(current_user.liked_by)

    matches = set(current_user.likes) & set(current_user.liked_by)

    return render_template('index.html', current_user=current_user, random_user=random_user, matches=matches)

@app.route('/like/<id>')
@require_login
def like(id):
    token = request.cookies.get('token')
    current_user = User.find_by_token(token)
    liked_user = User.query.filter_by(id=id).first()
    current_user.likes.append(liked_user)
    db.session.commit()
    flash('<3 {} <3'.format(liked_user.username))
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
@stop_logged_users
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']

        try:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            flash('Error: {}'.format(e))
            return redirect(request.url)

@app.route('/login', methods=['GET', 'POST'])
@stop_logged_users
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = json.loads(request.data.decode('ascii'))
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            return jsonify({'token': None})
        token = user.generate_token()
        return jsonify({'token': token.decode('ascii')})
