#!/usr/bin/env python3
"""Use _ or gettext function to parametrize templates.
   Use message IDs home_title and home_header.
"""
from flask import Flask, request, render_template
from flask_babel import Babel, _
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Match client's preferred language with
       supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run
