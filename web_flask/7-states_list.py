#!/usr/bin/python3
"""
Flask web application                           """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/state_list')
def store():
    """
    Display states sorted by name
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontent
def teardown(exception):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
