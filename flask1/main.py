from flask import Flask
from flask import render_template, request, redirect, url_for
from post import Post

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('list_posts'))

@app.route('/posts')
def list_posts():
    return render_template('posts.html', posts=Post.all())

@app.route('/posts/<int:id>')
def show_post(id):
    post = Post.find(id)

    return render_template('post.html', post=post)

@app.route('/posts/<int:id>/edit')
def edit_post(id):
    post = Post.find(id)

    return render_template('post.html', post=post)

@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'GET':
        return render_template('new_post.html')
    elif request.method == 'POST':
        values = (None, request.form['name'], request.form['author'], request.form['content'])
        Post(*values).create()

        return redirect(url_for('list_posts'))

