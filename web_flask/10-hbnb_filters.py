#!/usr/bin/python3
"""
Flask web application                           """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/state_list')
def state_list():
    """
    Display states sorted by name
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route('cities_by_states')
def cities_by_states():
    """
    Display list of Cities
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.route('/states')
@app.route('/states/<id>')
def states_by_id(id=None):
    """
    Display cities by their id and cities
    or diplay states only
    """
    states = storage.all("State")
    if id is None:
        case = 1
        state = None
    else:
        by_id = "State." + str(id)
        if by_id in states.keys():
            state = states[state_id]
            case = 2
        else:
            case = 3
            state = None
    return render_template('9-states.html', state=state,
                           states=states.values(), case=case)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays the main HBnB filters HTML page
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontent
def teardown(exception):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
