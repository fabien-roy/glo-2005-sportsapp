from flask import render_template, request
from flask.views import View
from injector import inject

from app import users_blueprint
from app.users.exceptions import UserNotFoundException
from app.users.forms import UsersSearchForm
from app.users.repositories import UsersRepository


@users_blueprint.route('/users', methods=('GET', 'POST'))
def users(users_repository: UsersRepository):
    form = UsersSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_users = users_repository.get_all(form)
    else:
        all_users = users_repository.get_all(None)

    return render_template('users.html', users=all_users, form=form)


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
