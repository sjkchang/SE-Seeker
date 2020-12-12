from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, URL, ValidationError
from .. import db
from ..models.Internship import Internship


class InternshipForm(FlaskForm):
    
    """Form used to gather user input to add an internship 

    Raises:
        ValidationError: Raises validation error if user inputs an 
        invalid term or year, or if an internship with the url they 
        entered already exists in the database
    """
    
    company = StringField('Company', validators=[DataRequired(message="Company Name is Required")])
    term = StringField('Term', validators=[DataRequired(message="Enter Internship Term(ex. Summer, Fall, ect")])
    year = IntegerField('Year', validators=[DataRequired(message="Enter Valid Internship Year")])
    location = StringField('Location', validators=[DataRequired(message="Enter Internship Location")])
    additional_information = TextAreaField('Additional Information')
    url = StringField('URL', validators=[DataRequired(), URL(message="Enter Valid URL")])

    submit = SubmitField('Submit')

    def validate_term(self, term):
        if not (term.data == "Summer" or term.data == "Spring" or term.data == "Winter" or term.data == "Fall"):
            raise ValidationError("Please enter internship Term: Summer, Winter, Fall or Spring")

    def validate_url(self, url):
        internship = db.session.query(Internship).filter_by(link=url.data).first()
        if internship:
            raise ValidationError("An internship using that link already exists")

    def validate_year(self, year):
        if year.data > 2030 or year.data < 2020:
            raise ValidationError("That Year is not Valid")
