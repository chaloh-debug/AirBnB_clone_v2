#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask, render_template
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
