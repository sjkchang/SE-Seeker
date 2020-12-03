"""
routes.py
====================================
The url routes that render html templates, and handles forms and database manipulation
"""
from __future__ import print_function

from flask import current_app as app
from flask import render_template, url_for, redirect
from flask_login import current_user, login_required
from .. import db
from ..forms.InternshipForm import InternshipForm
from ..models.Internship import Internship


@app.route('/add-internship', methods=['GET', 'POST'])
@login_required
def add_internship():
    form = InternshipForm()
    if form.validate_on_submit():
        print(current_user)
        Internship.create(company=form.company.data, term=form.term.data, year=form.year.data, location=form.location.data,
                          additional_information=form.additional_information.data, link=form.url.data)
        return redirect(url_for('internships'))
    return render_template('add_internship.html', form=form, title='Add Internship')


@app.route('/internships')
def internships():
    internships = db.session.query(Internship).all()
    return render_template('internships.html', internships=internships, title='Internships')
