import uuid
import os

from flask import Flask
from flask import render_template, request, redirect, make_response, url_for
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from database import db_session, init_db
from login import login_manager
from models import User, UserLike
from utils import validate_file_type, split_in_groups


app = Flask(__name__)
# NEVER KEEP SECRET KEYS INSIDE YOUR PUBLIC CODE
app.secret_key = "ssucuuh398nuwetubr33rcuhne"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB
app.config['UPLOAD_FOLDER'] = '/tmp/flask/uploads'

login_manager.init_app(app)
init_db()

app.add_url_rule('/uploads/<filename>', 'uploaded_file', build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})


@app.teardown_appcontext
def shutdown_context(exception=None):
    db_session.remove()


@app.route('/', methods=['GET'])
@login_required
def homepage():
    return redirect(url_for('find_match'))


@app.route('/match', methods=['GET'])
@login_required
def find_match():
    suggestion = User.find_another_random(current_user)
    return render_template("match.html", suggestion=suggestion)


@app.route('/match', methods=['POST'])
@login_required
def match():
    if request.form["liked_user_id"] is not None:
        liked_user = int(request.form["liked_user_id"])
        user_like = UserLike(liked_by=current_user.id, liked_user=liked_user)
        current_user.likes.append(user_like)
        db_session.commit()
    return redirect(url_for('find_match'))


@app.route('/matches', methods=['GET'])
@login_required
def get_matches():
    likes = [like[1] for like in UserLike.find_matches(current_user)]
    return render_template("all_likes.html", likes=split_in_groups(likes))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        user = User(username=username, password=password)
        db_session.add(user)
        db_session.commit()
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    response = None
    if request.method == 'GET':
        response = make_response(render_template('login.html'))
    else:
        response = make_response(redirect(url_for('profile')))

        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            user.login_id = str(uuid.uuid4())
            db_session.commit()
            login_user(user)
    return response


@app.route("/logout")
@login_required
def logout():
    current_user.login_id = None
    db_session.commit()
    logout_user()
    return redirect(url_for('login'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'GET':
        return render_template("profile.html")
    elif request.method == 'POST':
        current_user.first_name = request.form['first_name']
        current_user.last_name = request.form['last_name']
        current_user.age = request.form['age']
        current_user.bio = request.form['bio']
        if 'profile_pic' in request.files and request.files['profile_pic']:
            upload = request.files['profile_pic']
            filename = secure_filename(upload.filename)
            if validate_file_type(filename, ["jpeg", "jpg", "png"]):
                upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                current_user.profile_pic = '/uploads/{}'.format(filename)
        db_session.commit()
        return redirect(url_for('profile'))


