#!/usr/bin/env python3
"""Instantiate the Babel object in your app.
   Store it in a module-level variable named babel"""

from flask import Flask
from flask_babel import Babel
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def home():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run
