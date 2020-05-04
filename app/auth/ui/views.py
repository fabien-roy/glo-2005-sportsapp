from abc import abstractmethod, ABCMeta

import datetime
import bcrypt
from flask import render_template, request, Blueprint, url_for, redirect, flash, session
from flask.views import View
from injector import inject

from app.auth.forms import LoginForm, RegisterForm
from app.users.models import User
from app.users.repositories import UserRepository

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/register', methods=('GET', 'POST'))
def register(users_repository: UserRepository):
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data,
                    first_name=form.first_name.data, last_name=form.last_name.data,
                    phone_number=form.telephone.data)
        users_repository.add(user)

        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


@auth_blueprint.route('/login', methods=('GET', 'POST'))
def login(users_repository: UserRepository):
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user_password = users_repository.get_password(form.username.data)
        decoded_password = (bcrypt.hashpw(form.password.data.encode('utf-8'),
                                          user_password.encode('utf-8'))).decode('utf-8')
        if user_password and decoded_password == user_password:
            user = users_repository.get(form.username.data)
            user.last_login_date = datetime.datetime.today()
            session['logged_in'] = True
            session['_user_id'] = user.username
            flash('You are now logged in as ' + session['_user_id'] + '.', 'success')
            return redirect(url_for('users.user_details', username=user.username), 302)

        flash('Login Unsuccessful. Please check email and password', 'error')

    return render_template('login.html', form=form)


@auth_blueprint.route('/logout', methods=('GET', 'POST'))
def logout():
    session['logged_in'] = False
    return redirect(url_for('search.search'))


class AuthView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
