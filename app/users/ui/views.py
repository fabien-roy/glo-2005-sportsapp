from abc import abstractmethod, ABCMeta

import bcrypt

from flask import render_template, request, Blueprint, url_for, redirect, flash
from flask.views import View
from injector import inject
from flask_login import login_user, current_user, logout_user, login_required

from app.users.exceptions import UserNotFoundException
from app.users.forms import UsersSearchForm, RegisterForm, LoginForm
from app.users.repositories import UserRepository
from app.users.models import User


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/users', methods=('GET', 'POST'))
def users(users_repository: UserRepository):
    form = UsersSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_users = users_repository.get_all(form)
    else:
        all_users = users_repository.get_all(None)

    return render_template('users.html', users=all_users, form=form, current_user=current_user)


@user_blueprint.route('/users/<username>')
def user_details(users_repository: UserRepository, username):
    try:
        user = users_repository.get(username)
    except UserNotFoundException:
        return render_template('404.html'), 404

    print(current_user)

    return render_template('user_details.html', user=user)


@user_blueprint.route('/register', methods=('GET', 'POST'))
def register(users_repository: UserRepository):
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data,
                    first_name=form.first_name.data, last_name=form.last_name.data, phone_number=form.telephone.data)
        users_repository.add(user)

        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


@user_blueprint.route('/login', methods=('GET', 'POST'))
def login(users_repository: UserRepository):
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('users.user'))

    if form.validate_on_submit():
        user_password = users_repository.get_password(form.username.data)
        if user_password and (bcrypt.hashpw(form.password.data.encode('utf-8'),
                                            user_password.encode('utf-8'))).decode('utf-8') == user_password:
            user = users_repository.get(form.username.data)
            user.is_authenticated = True
            login_user(user)
            flash('You are now logged in as ' + current_user.username + '.', 'success')
            return redirect(url_for('users.user_details', username=current_user.username))
        else:
            flash('Login Unsuccessful. Please check email and password', 'error')
    return render_template('login.html', form=form)


class UserView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
