#!/usr/bin/env python3
"""
Basic flask app
"""
from os import getenv
from flask_babel import Babel
from flask import (
    Flask,
    g,
    render_template,
    request)
app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    class config to set the languages and default time zone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user():
    """
    function that returns a user dictionary or None if the ID cannot be found
    """
    uid = request.args.get('login_as', None)
    if id is not None and int(uid) in users.keys():
        return users.get(int(uid))
    return None


@app.route('/')
def index() -> str:
    """
    function returns a basic html file
    """
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """
    function to determine the best match with our supported languages
    """
    if request.args.get("locale"):
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def before_request():
    """
    function to find a user if any, and set it as a global on flask.g.user
    """
    user = get_user()
    g.user = user


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
