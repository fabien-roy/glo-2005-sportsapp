from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class PracticeCentersSearchForm(FlaskForm):
    class Meta:
        csrf = False

    all = StringField('Any field', validators=[Length(max=200)])
    name = StringField('Name', validators=[Length(max=50)])
    email = StringField('Email', validators=[Length(max=100)])
    web_site = StringField('Web site', validators=[Length(max=200)])
    phone_number = StringField('Phone number', validators=[Length(max=20)])
    submit = SubmitField('Search')
