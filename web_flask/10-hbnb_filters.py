#!/usr/bin/python3
"""
Start a Flask web application on localhost.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)

@app.teardown_appcontext
def close(self):
    """
    Method to close the session.
    """
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays an HTML page with filters from web static.
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
