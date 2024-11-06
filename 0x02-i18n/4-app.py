#!/usr/bin/env python3
"""Implement a way to force a particular locale by passing the
   locale=fr parameter to yout app's URLs.
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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run
