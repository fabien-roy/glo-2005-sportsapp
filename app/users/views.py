from flask import render_template, Blueprint
from flask.views import View
from injector import inject

from app.users.exceptions import UserNotFoundException
from app.users.repositories import UserRepository

users_blueprint = Blueprint('users', __name__)


# TODO : Make users query params for search
@users_blueprint.route('/users/')
def users(user_repository: UserRepository):
    all_users = user_repository.get_all()
    return render_template('users.html', users=all_users)


@users_blueprint.route('/users/<username>')
def user_details(user_repository: UserRepository, username):
    try:
        user = user_repository.get(username)
    except UserNotFoundException:
        return render_template('404.html'), 404

    return render_template('user_details.html', user=user)


class UserView(View):
    def dispatch_request(self):
        pass

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
