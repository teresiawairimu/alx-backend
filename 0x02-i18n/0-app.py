#!/usr/bin/env python3
"""Set up a basic flask app. Create a single route and
   an index.html template"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Renders the index.html template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run
