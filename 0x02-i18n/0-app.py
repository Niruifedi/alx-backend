#!/usr/bin/env python3
"""
Basic flask app
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    """
    ffunction returns a basic html file
    """
    return render_template("0-index.html")
