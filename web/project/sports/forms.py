from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, length

class SportsSearchForm(Form):
    name = StringField('Name', validators=[DataRequired(), length(min=2, max=50) ])
