#!/usr/bin/python3
"""
a script that starts up a Flask web application
"""


from flask import Flask
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


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_is_cool(text):
    """ replies to "/python/(<text>"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
