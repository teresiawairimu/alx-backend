#!/usr/bin/env python3
"""Create a get_locale function with babel.localeselector
   decorator.
"""
from flask import Flask, request
from flask_babel import Babel
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
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run
