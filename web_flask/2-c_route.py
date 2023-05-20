#!/usr/bin/python3

"""
This is a Flask web application.

It provides the following routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"
- /c/<text>: Displays "C " followed by the value of the text variable
  (replace underscore _ symbols with a space)

The application listens on 0.0.0.0, port 5000.
"""

from flask import Flask, request

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


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """
    Route handler for '/c/<text>' URL.
    Displays "C " followed by the value of the text variable.

    Args:
        text (str): The text value from the URL.

    Returns:
        str: The response string.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
