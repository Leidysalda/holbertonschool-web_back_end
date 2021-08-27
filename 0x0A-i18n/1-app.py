#!/usr/bin/env python3
""" Basic Flask app
"""


from flask import Flask, render_template
from os import getenv
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Has a languages
    """
    LANGUAJES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Index
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
