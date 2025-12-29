from app import create_app
from flask import render_template, send_from_directory


app = create_app()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/children")
def children():
    return render_template("children.html")


@app.route("/widows")
def widows():
    return render_template("widows.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/mission_vision")
def mission_vision():
    return render_template("mission_vision.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory('static/images/', 'favicon.ico')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)