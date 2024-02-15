#!/usr/bin/python3
"""
Start a Flask web application on localhost.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a string.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns HBNB.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_print(text):
    """
    Function that returns a C(str) and user text.
    """
    result = text.replace('_', ' ')
    return "C {}".format(result)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_print(text="is cool"):
    """
    Function that returns a Python(str) and user text.
    """
    result = text.replace('_', ' ')
    return "Python {}".format(result)


@app.route('/number/<n>', strict_slashes=False)
def print_number(n):
    """
    Function that returns a string only if n is an integer (number).
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_number_template(n):
    """
    Function that displays an HTML page only if n is an integer.
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_number_odd_or_even(n):
    """
    Function that displays an HTML page only if n is an integer.
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
