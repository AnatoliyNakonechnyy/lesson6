from flask import Blueprint

post_bp = Blueprint("post", __name__, url_prefix="/post")


@post_bp.route("/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"
