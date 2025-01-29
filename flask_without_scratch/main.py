from flask import Flask, render_template, request, flash, redirect, url_for, abort

import service
from database.model import Post
from format_utils import date_from_datetime
from service import get_posts

first = Flask(__name__)
first.secret_key = "your-secret-key"

generally_posts = []


@first.template_filter("date_format")
def date_format(date):
    return date_from_datetime(date)


@first.route("/guest/")
def hello_any_guest():
    return "Hello any"


@first.route("/guest/<guest>")
def hello_specific_guest(guest):
    return f"Hello {guest} as Guest"


@first.route("/")
def index():
    # return 'Hello, World!'
    # posts = get_posts()
    posts = generally_posts
    return render_template("index.html", posts=posts)


@first.route("/post/<int:post_id>")
def post(post_id):
    posts = get_posts(post_id)
    if not posts:
        abort(404)
    return render_template("post.html", post=posts[0])


@first.route("/post/create", methods=("GET", "POST"))
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        else:
            service.create(Post(title, content))
            return redirect(url_for("index"))
    return render_template("create_post.html")


@first.route("/post/edit/<int:id>", methods=("GET", "POST"))
def edit_post(id):
    posts = get_posts(id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        else:
            service.update(Post(title, content, id=id))
            return redirect(url_for("index"))
    if not posts:
        abort(404)
    return render_template("edit.html", post=posts[0])


@first.route("/delete/<int:id>", methods=("POST",))
def delete_post(id):
    post = get_posts(id)
    if not post:
        abort(404)
    service.delete(id)
    flash(f"{post[0].title} was successfully deleted!")
    return redirect(url_for("index"))


if __name__ == "__main__":
    first.run(host="0.0.0.0", port=8000, debug=True)
