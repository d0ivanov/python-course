import json
import uuid

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


def get_id():
    return str(uuid.uuid1())


class Post(object):

    def __init__(self, post_id, title, content):
        self.id = post_id
        self.title = title
        self.content = content

    def to_dict(self):
        return self.__dict__


# id -> Post(...)
POSTS = {}


@app.route("/api/posts", methods = ["POST"])
def create_post():
    post_data = request.get_json(force=True, silent=True)
    if post_data == None:
        return "Bad request", 400
    post_id = get_id()
    post = Post(post_id, post_data["title"], post_data["content"])
    POSTS[post_id] = post
    return json.dumps(post.to_dict()), 201


@app.route("/api/posts", methods = ["GET"])
def list_posts():
    result = {"result": []}
    for post in POSTS.values():
        result["result"].append(post.to_dict())
    return json.dumps(result)


@app.route("/api/posts/<post_id>", methods = ["GET"])
def get_post(post_id):
    if post_id in POSTS:
        return json.dumps(POSTS[post_id].to_dict())
    return "", 404


@app.route("/api/posts/<post_id>", methods = ["DELETE"])
def delete_post(post_id):
    if post_id in POSTS:
        del POSTS[post_id]
        return ""
    return "", 404


@app.route("/api/posts/<post_id>", methods = ["PATCH"])
def update_post(post_id):
    post_data = request.get_json(force=True, silent=True)
    if post_data == None:
        return "Bad request", 400
    if post_id in POSTS:
        post = POSTS[post_id]
        if "title" in post_data:
            post.title = post_data["title"]
        if "content" in post_data:
            post.content = post_data["content"]
        return json.dumps(post.to_dict())
    return "", 404


@app.route("/", methods = ["GET"])
def posts():
    return render_template("index.html")


@app.route("/posts/<post_id>", methods = ["GET"])
def view_post(post_id):
    if post_id in POSTS:
        return render_template("post.html", post=POSTS[post_id])
    return "", 404







