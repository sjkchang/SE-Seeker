"""
routes.py
====================================
The url routes that render html templates, and handles forms and database manipulation
"""


from __future__ import print_function
from flask import current_app as app
from flask import render_template, url_for, flash, redirect, request
from . import db
from .forms import InternshipForm
from .models import Internship

@app.route('/')
@app.route('/home')
def home():
    """
    Route for the home page
    """
    return render_template('home.html')

@app.route('/add_internship', methods=['GET', 'POST'])
def add_internship():
    form = InternshipForm()
    if form.validate_on_submit():
        internship = Internship(company=form.company.data, term=form.term.data, year=form.year.data, additional_info=form.additional_information.data)
        db.session.add(internship)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_internship.html', form=form, title='Add Int')


@app.route('/internships')
def internships():
    internships = db.session.query(Internship)
    print(internships)
    return render_template('internships.html', internsips=internships)