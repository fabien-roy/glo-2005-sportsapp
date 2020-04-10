from wtforms import StringField
from wtforms.validators import Length

from app.search.forms import GeneralSearchForm


class ShopsSearchForm(GeneralSearchForm):
    name = StringField('Name', validators=[Length(max=50)])
    email = StringField('Email', validators=[Length(max=100)])
    web_site = StringField('Web site', validators=[Length(max=200)])
    phone_number = StringField('Phone number', validators=[Length(max=20)])
