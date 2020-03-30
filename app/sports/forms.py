from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class SportsSearchForm(FlaskForm):
    class Meta:
        csrf = False

    name = StringField('Name', validators=[Length(max=50)])
    submit = SubmitField('Search')
