#!/usr/bin/python3
"""Start a Flask web application on localhost"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def print_c(text):
    result= text.result('_', ' ')
    return("C {}".format.string(result))

@app.route('/python/<text>', strict_slashes=False)
def print_python(text= "Is Cool"):
    result= text.result('_', ' ')
    return("Python {}".format.string(result))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
