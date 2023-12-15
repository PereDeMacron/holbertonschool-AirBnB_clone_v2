#!/usr/bin/python3
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

@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    if type(n)== int:
        return("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
