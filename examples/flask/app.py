import json
import uuid

from flask import Flask
from flask import request
from flask import render_template

from model.post import Post
from errors import register_error_handlers


app = Flask(__name__)

register_error_handlers(app)


@app.route("/api/posts", methods = ["POST"])
def create_post():
    post_data = request.get_json(force=True, silent=True)
    if post_data == None:
        return "Bad request", 400
    post = Post(post_data["title"], post_data["content"])
    post.save()
    return json.dumps(post.to_dict()), 201


@app.route("/api/posts", methods = ["GET"])
def list_posts():
    result = {"result": []}
    for post in Post.all():
        result["result"].append(post.to_dict())
    return json.dumps(result)


@app.route("/api/posts/<post_id>", methods = ["GET"])
def get_post(post_id):
    return json.dumps(Post.find(post_id).to_dict())


@app.route("/api/posts/<post_id>", methods = ["DELETE"])
def delete_post(post_id):
    Post.delete(post_id)
    return ""


@app.route("/api/posts/<post_id>", methods = ["PATCH"])
def update_post(post_id):
    post_data = request.get_json(force=True, silent=True)
    if post_data == None:
        return "Bad request", 400

    post = Post.find(post_id)
    if "title" in post_data:
        post.title = post_data["title"]
    if "content" in post_data:
        post.content = post_data["content"]
    return json.dumps(post.save().to_dict())


@app.route("/", methods = ["GET"])
def posts():
    return render_template("index.html")


@app.route("/posts/<post_id>", methods = ["GET"])
def view_post(post_id):
    return render_template("post.html", post=Post.find(post_id))


