from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint, session
from flask_login import current_user
from flask.views import View
from injector import inject

from app.users.exceptions import UserNotFoundException
from app.users.forms import UsersSearchForm
from app.users.repositories import UserRepository

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/users', methods=('GET', 'POST'))
def users(users_repository: UserRepository):
    form = UsersSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_users = users_repository.get_all(form)
    else:
        all_users = users_repository.get_all(None)

    return render_template('users.html', users=all_users, form=form)


@user_blueprint.route('/users/<username>')
def user_details(users_repository: UserRepository, username):
    try:
        user = users_repository.get(username)
    except UserNotFoundException:
        return render_template('404.html'), 404

    return render_template('user_details.html', user=user)


class UserView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
