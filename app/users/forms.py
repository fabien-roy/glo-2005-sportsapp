from wtforms import StringField
from wtforms.validators import Length

from app.search.forms import GeneralSearchForm


class UsersSearchForm(GeneralSearchForm):
    username = StringField('Username', validators=[Length(max=50)])
    email = StringField('Email', validators=[Length(max=100)])
    first_name = StringField('First name', validators=[Length(max=50)])
    last_name = StringField('Last name', validators=[Length(max=50)])
    phone_number = StringField('Phone number', validators=[Length(max=20)])
