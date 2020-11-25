from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from ..models.User import User


class RegistrationForm(FlaskForm):
    """
    A registration FlaskForm
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8),
                                    EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if User.usernameExists(username.data):
            raise ValidationError('An account already exists with that username. Please chose another.')

    def validate_email(self, email):
        if User.emailExists(email.data):
            raise ValidationError("An account already exists with that email. Please chose another")
