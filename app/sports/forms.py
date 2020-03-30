from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import length


class SportsSearchForm(FlaskForm):
    class Meta:
        csrf = False

    name = StringField('Name', validators=[length(max=50)])
    submit = SubmitField("Search")
