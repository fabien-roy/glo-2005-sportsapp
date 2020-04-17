from wtforms import StringField
from wtforms.validators import Length

from app.search.forms import GeneralSearchForm


class SportSearchForm(GeneralSearchForm):
    name = StringField('Name', validators=[Length(max=50)])
