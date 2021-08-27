#!/usr/bin/env python3
""" Basic Flask app
"""
from flask import Flask, render_template, request, g
from os import getenv
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Has a languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

    
@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Index
    """
    return render_template('5-index.html', locale=get_locale())


@babel.localeselector
def get_locale():
    """ get locale 
    """
    locale = request.args.get('locale')
    languages = app.config['LANGUAGES']
    if locale in languages:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """ Get User
    """
    try:
        myId = int(request.args.get('login_as'))
    except (ValueError, TypeError):
        return None
    if myId in users.keys():
        return users.get(myId)
    return None

@app.before_request
def before_request():
    """ Result
    """
    user = get_user()
    g.user = user

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
