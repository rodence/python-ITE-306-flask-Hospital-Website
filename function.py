from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/treatment")
def treatment():
    return render_template("treatment.html")


@app.route("/partner")
def partner():
    return render_template("partner.html")


@app.route("/service")
def service():
    return render_template("service.html")


if __name__ == "__main__":
    app.run(debug=True)