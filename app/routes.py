from flask import render_template, send_from_directory
from flask import Blueprint


bp = Blueprint('views', __name__, url_prefix='/')


@bp.route("/")
def home():
    title = "Home of Love Orphanage"
    return render_template("index.html", title=title)


@bp.route("/children")
def children():
    title = "Children"
    return render_template("children.html", title=title)


@bp.route("/children/<child>")
def child(child):
    title = child
    if (child == "annabel"):
        return render_template("annabel.html", title=title)


@bp.route("/widows")
def widows():
    title = "Widows"
    return render_template("widows.html", title=title)


@bp.route("/donate")
def donate():
    title = "Donate"
    return render_template("donate.html", title=title)


@bp.route("/contact")
def contact():
    title = "Contact"
    return render_template("contact.html", title=title)


@bp.route("/mission_vision")
def mission_vision():
    title = "Mission&Vision"
    return render_template("mission_vision.html", title=title)


@bp.route("/favicon.ico")
def favicon():
    return send_from_directory('static/images/', 'favicon.ico')