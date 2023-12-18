#!/usr/bin/python3
"""Start a Flask web application on localhost"""
from flask import Flask
from flask import render_template

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


@app.route('/number/<n>', strict_slashes=False)
def print_number(n):
    if type(n)== int:
        return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_number(n):
    if type(n)== int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_number(n):
    if type(n)== int:
        return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
