from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Home",
        username="Deepshika",
        message="Welcome to my first Flask website!"
    )

@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About",
        college="SEC",
        course="B.Tech Information Technology"
    )

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/submit", methods=["POST"])

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    return render_template("result.html", name=name)
if __name__ == "__main__":
    app.run(debug=True)