from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, URL


class InternshipForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired(message="Enter Company Name")])
    term = StringField('Term', validators=[DataRequired(message="Enter Internship Term(ex. Summer, Fall, ect")])
    year = IntegerField('Year', validators=[DataRequired(message="Enter Internship Year")])
    location = StringField('Location', validators=[DataRequired(message="Enter Internship Location")])
    additional_information = TextAreaField('Additional Information', validators=[DataRequired(message="Enter Additional Info (N/A) if none")])
    url = StringField('URL', validators=[DataRequired(), URL(message="Enter Valid URL")])

    submit = SubmitField('Submit')
