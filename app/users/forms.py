from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    last_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    first_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=50)])
    telephone = StringField('Telephone number', validators=[DataRequired(), Length(min=10, max=20)])


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired()])


class EditUserPasswordForm(Form):
    new_password = PasswordField('New Password', validators=[])
    new_confirm_password = PasswordField('Repeat New Password', validators=[EqualTo('new_password')])