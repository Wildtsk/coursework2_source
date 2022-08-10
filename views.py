import logging
from json import JSONDecodeError
from os import abort

from flask import Blueprint, render_template, request

from utils import get_post_by_pk, get_posts_all, get_comments_by_post_id, search_for_posts, get_posts_by_user

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def mane_page():
    posts = get_posts_all()
    return render_template("index.html", posts=posts, len=len(posts))


@main_blueprint.route("/post/<postid>")
def post_by_id_page(postid):
    post = get_post_by_pk(postid)
    comments_post = get_comments_by_post_id(postid)
    len_comment_post = len(comments_post)
    return render_template("post.html", post=post, comments=comments_post, len_comment_post=len_comment_post)


@main_blueprint.route("/search/")
def search_page():
    search_query = request.args.get("search_query")
    logging.info('Поиск выполняется')
    posts = search_for_posts(search_query)
    if posts != "418":
        return render_template("search.html", query=search_query, posts=posts)
    return abort(418)


@main_blueprint.errorhandler(500)
def bar(error):
    return '418 Im a teapot', 418


@main_blueprint.route("/user-feed/<username>")
def post_by_username_page(username):
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, name=username)
