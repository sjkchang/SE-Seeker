from __future__ import print_function
from flask import current_app as app
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, current_user, login_required, login_manager
from .. import db, login_manager, bcrypt


@app.route('/home')
def home():
    """
    Route for the home page
    """
    link = "https://www.google.com/"
    return render_template('home.html', link=link, current_user=current_user)
