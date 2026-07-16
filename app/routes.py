from collections import namedtuple
from datetime import datetime
import os
from flask import render_template, send_from_directory
from flask import Blueprint
from app import db
from app.models import Blog


bp = Blueprint('views', __name__, url_prefix='/')


@bp.route("/")
def home():
    title = "Home of Love Orphanage"
    return render_template("index.html", title=title)


@bp.route("/children")
def children():
    title = "Children"
    return render_template("children.html", title=title)


@bp.route("/blog")
def blog():
    stmt = (db.select(Blog.title, Blog.date, Blog. author, Blog.id)
                      .select_from(Blog)
                      .order_by(Blog.date.desc()))
    blogs = db.session.execute(stmt).all()
    rows = list()
    for blog in blogs:
        blog = list(blog)
        blog[1] = iso2mdy(blog[1])
        rows.append(blog)
    templateData = {"rows": rows}
    templateData['title'] = " HOLO Blog"
    return render_template('blog.html', **templateData)


@bp.route("/blog/<blogid>")
def blogpost(blogid):
    Post  = namedtuple('Post', ['title', 'body', 'date', 'id', 'pagecss', 'author'])
    stmt = (db.select(Blog.title, Blog.body, Blog.date, Blog.id, Blog.pagecss, Blog.author)
                      .select_from(Blog)
                      .where(Blog.id == blogid))
    blog = Post(*(db.session.execute(stmt).all()[0]))
    blog = blog._replace(date=iso2mdy(blog.date))
    templateData = {"blogdata": blog}
    templateData['title'] = "Blog"
    return render_template('blogpost.html', **templateData)


@bp.route("/children/<child>")
def child(child):
    title = child
    if (child == "annabel"):
        return render_template("annabel.html", title=title)
    elif (child == 'benjamin'):
        return render_template("benjamin.html", title=title)
    elif (child == 'abraham'):
        return render_template("abraham.html", title=title)
    elif (child == 'deborah'):
        return render_template("deborah.html", title=title)
    elif (child == 'jane'):
        return render_template("jane.html", title=title)

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

@bp.route("/location")
def location():
    title = "Location"
    return render_template("location.html", title=title)

@bp.route("/sitemap.xml")
def sitemap():
    return send_from_directory('static/', 'sitemap.xml')


@bp.route("/robots.txt")
def robots():
    return send_from_directory('static/', 'robots.txt')


@bp.route("/favicon.ico")
def favicon():
    return send_from_directory('static/images/', 'favicon.ico')

def iso2mdy(iso_date):
    return datetime.fromisoformat(iso_date).strftime("%B %d, %Y")