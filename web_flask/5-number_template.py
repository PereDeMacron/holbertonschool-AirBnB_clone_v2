#!/usr/bin/python3
"""Start a Flask web application on localhost"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a string: 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string: 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_print(text):
    """
    Function that returns a string with 'C' followed by the user text.
    Replaces underscores in the user text with spaces.
    """
    result = text.replace('_', ' ')
    return "C {}".format(result)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_print(text="is cool"):
    """
    Function that returns a string with 'Python' followed by the user text.
    Replaces underscores in the user text with spaces.
    """
    result = text.replace('_', ' ')
    return "Python {}".format(result)


@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    """
    Function that returns a string stating
        that the provided number is a number.
    Only works if the provided value is an integer.
    """
    if type(n) == int:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_number_template(n):
    """
    Function that displays an HTML page with the provided number.
    Only works if the provided value is an integer.
    Uses the '5-number.html' template for rendering.
    """
    if type(n) == int:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
