#!/usr/bin/python3
"""Start a Flask web application on localhost"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns a string"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB string"""
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_print(text):
    """Function that returns a C string"""
    result = text.replace('_', ' ')
    return "C {}".format(result)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_print(text="is cool"):
    """Function that returns a Python string"""
    result = text.replace('_', ' ')
    return "Python {}".format(result)


@app.route('/number/<n>', strict_slashes=False)
def print_number(n):
    if type(n)== int:
        """Function that returns a string only if n is a number"""
        return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_number(n):
    if type(n)== int:
        """Function that displays a HTML page only if n is an int"""
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_number(n):
    if type(n)== int:
        """Function that displays a HTML page only if n is an int"""
        return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
