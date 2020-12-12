from __future__ import print_function
from flask import current_app as app
from flask import render_template, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required, login_manager
from .. import login_manager, bcrypt
from ..forms.LoginForm import LoginForm
from ..forms.RegistrationForm import RegistrationForm
from ..forms.UpdateAccountForm import UpdateAccountForm
from ..forms.DeleteForm import DeleteForm
from ..models.User import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Page for loging in
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
@login_required
def logout():
    """Route for login out
    """
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Page for Registering new user
    """
    if current_user.is_authenticated:
        redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        User.create(form.username.data, form.email.data, form.password.data)
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)


@app.route('/edit-account', methods=['GET', 'POST'])
def editAccount():
    """Page for editing an account
    """
    if not current_user.is_authenticated:
        redirect(url_for('home'))
    form = UpdateAccountForm()
    if form.validate_on_submit():
        User.edit(current_user.id, form.username.data, form.email.data, form.password.data)
        return redirect(url_for('home'))
    return render_template('editAccount.html', title='Edit Account', form=form, current_user=current_user)


@app.route('/delete-account', methods=['GET', 'POST'])
def deleteAccount():
    """Page to delete an account
    """
    if not current_user.is_authenticated:
        redirect(url_for('home'))
    deleteForm = DeleteForm()
    if deleteForm.validate_on_submit():
        User.delete(current_user)
        return redirect(url_for('login'))
    return render_template('delete_account.html', title='Delete Account', current_user=current_user, deleteForm=deleteForm)
