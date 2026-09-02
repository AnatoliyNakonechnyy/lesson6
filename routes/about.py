from flask import Blueprint, render_template

about_bp = Blueprint("about", __name__, url_prefix="/about")


@about_bp.route("/about")
def about():
    """
    Render the about page."""
    return render_template("pages/about.html")
