from wtforms import StringField
from wtforms.validators import Length

from app import GeneralSearchForm


class SportsSearchForm(GeneralSearchForm):
    name = StringField('Name', validators=[Length(max=50)])
