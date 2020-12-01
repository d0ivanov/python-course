from flask import Flask
from flask import render_template, request, redirect, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer
from itsdangerous import SignatureExpired, BadSignature
from werkzeug.security import generate_password_hash, check_password_hash

import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# NEVER KEEP SECRET KEYS INSIDE YOUR PUBLIC CODE
app.secret_key = "ssucuuh398nuwetubr33rcuhne"
db = SQLAlchemy(app)


def generate_token(user, secret, expires_in=600):
    s = TimedJSONWebSignatureSerializer(secret, expires_in)
    return s.dumps({'username': user.username})


def verify_token(token):
    s = TimedJSONWebSignatureSerializer(app.secret_key)
    try:
        s.loads(token)
    except SignatureExpired:
        print("here 1")
        return False
    except BadSignature:
        print("here 2")
        return False
    return True


def current_user(token):
    s = TimedJSONWebSignatureSerializer(app.secret_key)
    print(s.loads(token))
    parsed_token = s.loads(token)
    username = parsed_token['username']
    return User.query.filter_by(username=username).first()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(120), unique=False, nullable=True) 
    last_name = db.Column(db.String(120), unique=False, nullable=True) 
    age = db.Column(db.Integer(), unique=False, nullable=True) 

    def __init__(self, **kwargs):
        if 'password' in kwargs:
            kwargs['password'] = generate_password_hash(kwargs['password'])
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    response = None
    if request.method == 'GET':
        response = make_response(render_template('login.html'))
    else:
        response = make_response(redirect('/'))

        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            token = generate_token(user, app.secret_key, expires_in=99999)
            response.set_cookie('token', token)
    return response


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    auth_token = request.cookies['token']
    if auth_token is not None and not verify_token(auth_token):
        return redirect('/login')
    user = current_user(auth_token)

    if request.method == 'GET':
        return render_template("profile.html", user=user)
    elif request.method == 'POST':
        first_name = request.form['first_name']
        if first_name != user.first_name:
            user.first_name = first_name
        last_name = request.form['last_name']
        if last_name != user.last_name:
            user.last_name = last_name
        age = request.form['age']
        if age != user.age:
            user.age = age
        db.session.commit()
        return redirect('/profile')


