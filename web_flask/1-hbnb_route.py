#!/usr/bin/python3

"""
This is a simple Flask web application.

It provides two routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"

The application listens on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Route handler for the root URL.
    Displays "Hello HBNB!".

    Returns:
        str: The response string.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for '/hbnb' URL.
    Displays "HBNB".

    Returns:
        str: The response string.
    """
    return 'HBNB'


if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
