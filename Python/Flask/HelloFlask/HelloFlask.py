from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    return f"hello Flask"


@app.route("/<subpage>")
def hello_subpage(subpage):
    return f"hello {subpage}"


if __name__ == '__main__':
    app.run()