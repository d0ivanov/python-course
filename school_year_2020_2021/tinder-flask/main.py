from flask import Flask
from flask import render_template, request, flash, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

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

        try:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            flash('Error: {}'.format(e))
            return redirect(request.url)

@app.route('/login', methods=['GET', 'POST'])
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
