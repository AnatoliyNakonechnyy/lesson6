from flask import Blueprint, render_template

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/<string:username>")
def show_user_profile(username):
    return render_template(
        "components/user_profile.html",
        user={
            "username": username,
            "email": "user@example.com",
            "bio": "This is a simple user bio.",
            "profile_picture_url": None,
            "posts": [
                {
                    "title": "First Post",
                    "content": "This is the content of the first post.",
                },
                {
                    "title": "Second Post",
                    "content": "This is the content of the second post.",
                },
            ],
            "picture_url": "../static/images/user.jpg",
        },
    )
