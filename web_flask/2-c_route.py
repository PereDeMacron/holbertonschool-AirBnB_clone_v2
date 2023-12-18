#!/usr/bin/python3
<<<<<<< HEAD
from flask import Flask

=======
'''starts a Flask web application '''

from flask import Flask
>>>>>>> 1aaa358ba65a997b4545212c72aaf91d8fd849f5

app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_hbnb():
    return("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def print_c(text):
    result= text.result('_', ' ')
    return("C {}".format.string(result))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
=======
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Function that display HBNB '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 1aaa358ba65a997b4545212c72aaf91d8fd849f5
