from __future__ import print_function
from flask import current_app as app
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, current_user, login_required, login_manager
from .. import db, login_manager, bcrypt
from ..forms.LoginForm import LoginForm
from ..forms.RegistrationForm import RegistrationForm
from ..forms.UpdateAccountForm import UpdateAccountForm
from ..models.User import User


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Route for the login page
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        flash('Email or Pasword is invalid', 'error')
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
@login_required
def logout():
    """
    Route to logout user, redirects to login
    """
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Route for the registration page
    """
    if current_user.is_authenticated:
        redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        User.create(form.username.data, form.email.data, form.password.data)
        flash('Account Created, please sign in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)
