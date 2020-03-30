from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class PracticeCentersSearchForm(FlaskForm):
    class Meta:
        csrf = False


class PracticeCentersGeneralSearchForm(PracticeCentersSearchForm):
    all = StringField('Any field', validators=[InputRequired(), Length(max=200)])
    submit = SubmitField('Search')


class PracticeCentersSpecificSearchForm(PracticeCentersSearchForm):
    name = StringField('Name', validators=[Length(max=50)])
    email = StringField('Email', validators=[Length(max=100)])
    web_site = StringField('Web site', validators=[Length(max=200)])
    phone_number = StringField('Phone number', validators=[Length(max=20)])
    submit = SubmitField('Search')


def create_practice_centers_form(form=None):
    if len(form) > 0:
        if form.all is None:
            return PracticeCentersSpecificSearchForm(form)
        else:
            return PracticeCentersGeneralSearchForm(form)
