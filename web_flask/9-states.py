#!/usr/bin/python3
"""
starts up a flask webserver
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays a page with a unordered list of all States.
    States are sorted by names
    """
    states = storage.all(State)
    return render_template("9-states.html", state=states)

        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all(State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
