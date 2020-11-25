from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from ..models.User import User


class LoginForm(FlaskForm):
    """
    A login FlaskForm
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_password(self, password):
        if not (User.emailExists(self.email.data) and User.passwordMatches(self.email.data, self.password.data)):
            raise ValidationError('No account exists with that email and password combination. Please try again.')

    def validate_email(self, email):
        if not User.emailExists(email.data):
            raise ValidationError("No account exists with that email. Enter a different one, or create an new account.")
