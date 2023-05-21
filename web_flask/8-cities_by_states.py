#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask, render_template, escape
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    return hello hbnb
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    returns hbnb
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """
    display “C ” followed by the value
    of the text variable
    """
    return "C {}".format(text).replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def py_text(text="is cool"):
    """
    display “Python ”, followed by the
    value of the text variable
    """
    return "Python {}".forma(text).replace('_', ' ')


@app.route('/number/<int:n>')
def n_int(n):
    """
    display “n is a number” only if
    n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def n_template(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list')
def states_list():
    """
    Displays available states
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """
    Displays available states
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_app(exception):
    """
    closes current sqlalchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
