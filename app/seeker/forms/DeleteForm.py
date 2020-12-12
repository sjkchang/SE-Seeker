from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_login import current_user
from ..models.User import User


class DeleteForm(FlaskForm):
    """ This is a Form that is used to get the current user to enter their 
        password and doesnt validate if the password doesnt match the one in
        the database

    Raises:
        ValidationError: Raises a validation error if the password the user 
        entered doesn't match their password in the database
    """
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Delete Account')

    def validate_password(self, password):
        if not User.passwordMatchesID(current_user.id, password.data):
            raise ValidationError('That is not your password. Please retry')
