#!/usr/bin/python3
"""
a script that starts up a Flask web application
"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ shown at root of the server"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ called at route /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """ replies /c/<text> url"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/<text>", strict_slashes=False)
def py_is_cool(text="is cool"):
    """ replies to "/python/<text>"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """ replies 'n is a number if it is an integer"""
    num = int(n)
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ replies /number_template/<n> if n is an int"""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd(n):
    """checks if number is even or odd in the route
    if a positive integer is given
    """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
