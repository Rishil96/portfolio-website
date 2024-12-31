from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Home Page"


@app.route("/projects")
def projects():
    return "Projects Page"


@app.route("/contact")
def about():
    return "Contact Me Page"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
