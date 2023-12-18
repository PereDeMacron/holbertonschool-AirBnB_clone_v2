#!/usr/bin/python3
<<<<<<< HEAD
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return("HBNB")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
=======
""" flask import """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def dislplayHbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 1aaa358ba65a997b4545212c72aaf91d8fd849f5
