from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class SearchByName(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])

class SearchByAdress(Form):
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=50)])
