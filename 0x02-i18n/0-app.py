#!/usr/bin/env python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    """returns the html page for home"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run()
