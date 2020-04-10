from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class GeneralSearchForm(FlaskForm):
    class Meta:
        csrf = False

    any_field = StringField('Any field')
    submit = SubmitField('Search')
