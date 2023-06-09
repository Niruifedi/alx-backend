#!/usr/bin/env python3
"""
Basic flask app
"""
from os import getenv
from flask_babel import (
    Babel,
    _)
from flask import (
    Flask,
    render_template,
    request)
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    class config to set the languages and default time zone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """
    function returns a basic html file
    """
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """
    function to determine the best match with our supported languages
    """
    if request.args.get("locale"):
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
