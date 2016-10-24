from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # Creating route for landing page (index.html)
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)