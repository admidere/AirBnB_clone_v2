#!/usr/bin/python3

"""
This is a Flask web application.

It provides the following routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"
- /c/<text>: Displays "C ", followed by the value of the text variable
  (replace underscore _ symbols with a space)
- /python/(<text>): Displays "Python ", followed by the value of the text var
  (replace underscore _ symbols with a space)
  The default value of text is "is cool"
- /number/<n>: Displays "<n> is a number" only if n is an integer
- /number_template/<n>: Displays an HTML page only if n is an integer
  The HTML page contains an <h1> tag with the content "Number: n"

The application listens on 0.0.0.0, port 5000.
"""

from flask import Flask, render_template

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
def display_c(text):
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """
    Route handler for '/python/<text>' URL.
    Displays "Python " followed by the value of the text variable.

    Args:
        text (str): The text value from the URL.

    Returns:
        str: The response string.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Route handler for '/number/<n>' URL.
    Displays "<n> is a number" if n is an integer.

    Args:
        n (int): The number value from the URL.

    Returns:
        str: The response string.
    """
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    Route handler for '/number_template/<n>' URL.
    Displays an HTML page with "Number: n" if n is an integer.

    Args:
        n (int): The number value from the URL.

    Returns:
        str: The rendered HTML template.
    """
    if isinstance(n, int):
        return render_template('number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
