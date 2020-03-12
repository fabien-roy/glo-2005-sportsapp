from flask import render_template, Blueprint
from flask.views import View
from injector import inject

from app.users.exceptions import UserNotFoundException
from app.users.repositories import UsersRepository

users_blueprint = Blueprint('users', __name__)


# TODO : Make users query params for search
@users_blueprint.route('/users/')
def users(users_repository: UsersRepository):
    all_users = users_repository.get_all()
    return render_template('users.html', users=all_users)


@users_blueprint.route('/users/<username>')
def user_details(users_repository: UsersRepository, username):
    try:
        user = users_repository.get(username)
    except UserNotFoundException:
        return render_template('404.html'), 404

    return render_template('user_details.html', user=user)


class UserView(View):
    def dispatch_request(self):
        pass

    @inject
    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository
