from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


# TODO : Is this useful?
class SearchByName(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])


# TODO : Is this useful?
class SearchByAddress(Form):
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=50)])
