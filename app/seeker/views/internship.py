"""
routes.py
====================================
The url routes that render html templates, and handles forms and database manipulation
"""
from __future__ import print_function

import requests
from bs4 import BeautifulSoup
from flask import current_app as app
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, current_user, login_required, login_manager
from .. import db, login_manager, bcrypt
from ..forms.InternshipForm import InternshipForm
from ..models.Internship import Internship


@app.route('/add-internship', methods=['GET', 'POST'])
@login_required
def add_internship():
    form = InternshipForm()
    if form.validate_on_submit():
        Internship.create(company=form.company.data, term=form.term.data, year=form.year.data, location=form.location.data,
                          additional_information=form.additional_information.data, link=form.url.data)
        return redirect(url_for('home'))
    return render_template('add_internship.html', form=form, title='Add Internship')


@app.route('/internships')
def internships():
    internships = db.session.query(Internship).all()
    return render_template('internships.html', internships=internships)
