from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template(
        "index.html",
        title="Home",
        username="Deepshika",
        message="Welcome to my first Flask website!"
    )

@main.route("/about")
def about():
    return render_template(
        "about.html",
        title="About",
        college="SEC",
        course="B.Tech AI & DS"
    )

@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    return render_template("result.html", name=name)