#!/usr/bin/env python3
"""
Basic flask app
"""
from flask_babel import Babel
from flask import (
    Flask,
    render_template)
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    class config to set the languages and default time zone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
