from __future__ import print_function
from flask import current_app as app
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    """
    Route for the home page
    """
    return render_template('home.html')