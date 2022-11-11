#!/usr/bin/python3
""" sets up flask website"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_state():
    """ returns a list of states"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_down(ex):
    """ ran after every request. reloads
    the storage engine"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
