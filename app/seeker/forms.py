from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class InternshipForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    term = StringField('Term', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    additional_information = TextAreaField('Additional Information', validators=[DataRequired()])
    submit = SubmitField('Submit')
