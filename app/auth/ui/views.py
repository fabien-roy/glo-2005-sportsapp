from abc import abstractmethod, ABCMeta

import bcrypt
from flask import render_template, request, Blueprint, url_for, redirect, flash, session
from flask.views import View
from injector import inject

from app.admin.services import StatService
from app.auth.forms import LoginForm, RegisterForm
from app.users.exceptions import UserNotFoundException
from app.users.models import User
from app.users.repositories import UserRepository

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/register', methods=('GET', 'POST'))
def register(user_repository: UserRepository):
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data,
                    first_name=form.first_name.data, last_name=form.last_name.data,
                    phone_number=form.telephone.data)
        user_repository.add(user)

        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'), 302)

    return render_template('register.html', form=form)


@auth_blueprint.route('/login', methods=('GET', 'POST'))
def login(user_repository: UserRepository, stat_service: StatService):
    form = LoginForm(request.form)

    if form.validate_on_submit():
        try:
            user_password = user_repository.get_password(form.username.data)
        except UserNotFoundException:
            return login_unsuccessful()

        decoded_password = (bcrypt.hashpw(form.password.data.encode('utf-8'),
                                          user_password.encode('utf-8'))).decode('utf-8')
        if user_password and decoded_password == user_password:
            user = user_repository.get_touch(form.username.data)
            session['logged_in'] = True
            session['_user_id'] = user.username

            flash('You are now logged in as ' + session['_user_id'] + '.', 'success')
            stat_service.add_user_login()
            return redirect(url_for('users.user_details', username=user.username), 302)

        return login_unsuccessful()

    return render_template('login.html', form=form)


def login_unsuccessful():
    flash('Login Unsuccessful. Please check username and password', 'error')
    return redirect(url_for('auth.login'), 303)


@auth_blueprint.route('/logout', methods=('GET', 'POST'))
def logout():
    session['logged_in'] = False
    return redirect(url_for('search.search'), 302)


class AuthView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, user_repository: UserRepository, stat_service: StatService):
        self.user_repository = user_repository
        self.stat_service = stat_service
