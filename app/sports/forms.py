from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import length


class SportsSearchForm(Form):
    name = StringField('Name', validators=[length(max=50)])
    # TODO?
    # climate = StringField('Climate', validators=[length(max=50)])
    submit = SubmitField('Search')
