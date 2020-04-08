from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class GeneralSearchForm(FlaskForm):
    class Meta:
        csrf = False

    all = StringField('Any field')
    submit = SubmitField('Search')
