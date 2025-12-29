from flask import render_template, send_from_directory
from flask import Blueprint


bp = Blueprint('views', __name__, url_prefix='/')


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/children")
def children():
    return render_template("children.html")


@bp.route("/widows")
def widows():
    return render_template("widows.html")


@bp.route("/donate")
def donate():
    return render_template("donate.html")


@bp.route("/contact")
def contact():
    return render_template("contact.html")


@bp.route("/mission_vision")
def mission_vision():
    return render_template("mission_vision.html")


@bp.route("/favicon.ico")
def favicon():
    return send_from_directory('static/images/', 'favicon.ico')