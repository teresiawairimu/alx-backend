#!/usr/bin/env python3
"""Mock a database user table. Define a get_user function
   that returns a user dictionary or None if ID cannot be found
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, _
from config import Config

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Retrieve a user dictionary based on login_as parameter."""
    user_id = request.args.get("login_as")
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Set g.user to the logged-in user, if any."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Match client's preferred language with
       supported languages.
    """
    user = g.get('user')
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run
