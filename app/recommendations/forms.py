from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


def range_to_select_choices(items):
    choices = [(0, '0 star')]
    for item in items:
        choices.append((item, str(item) + ' stars'))
    return choices


class AddRecommendationForm(Form):
    note = SelectField('Note', choices=range_to_select_choices(range(1, 5)), validate_choice=False)
    comment = StringField('Comment', validators=[DataRequired(), Length(min=0, max=1000)],
                          render_kw={'placeholder': 'Comment'})
    submit = SubmitField('Add recommendation')
