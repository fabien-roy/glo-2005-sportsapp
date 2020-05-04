from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextField
from wtforms.validators import DataRequired, Length, EqualTo, Email


def range_to_select_choices(items):
    choices = []
    for item in items:
        choices.append((item, str(item)))
    return choices


class AddRecommendationForm(Form):
    note = SelectField('Note', validators=[DataRequired()],
                       choices=range_to_select_choices(range(0, 5)))
    comment = StringField('Comment', validators=[DataRequired(), Length(min=0, max=1000)],
                          render_kw={'placeholder': 'Comment'})
    submit = SubmitField('Add recommendation')
