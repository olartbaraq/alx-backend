#!/usr/bin/env python3
""" Starts a Flash Web Application """
from logging import config
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')

babel = Babel(app)


class Config(object):
    """class to configure available languages
    supported by the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def home_page() -> str:
    """returns homepage"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """function to invoke a request to select a language
    translation"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
