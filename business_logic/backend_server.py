from flask import Flask

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 12345

app = Flask(__name__)


import review_requests
import filter_requests


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=True)
