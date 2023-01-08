from flask import Flask
from myapp import __version__

app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>Running myapp v{__version__}.</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
