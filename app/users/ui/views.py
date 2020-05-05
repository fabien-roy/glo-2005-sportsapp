from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask.views import View
from flask_paginate import get_page_args, Pagination
from injector import inject

from app.users.exceptions import UserNotFoundException
from app.users.forms import UserSearchForm
from app.users.repositories import UserRepository

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/users', methods=('GET', 'POST'))
def users(user_repository: UserRepository):
    form = UserSearchForm(request.form)
    request_form = form if request.method == 'POST' and form.validate_on_submit() else None

    page, per_page, offset = get_page_args()
    total = user_repository.get_count(request_form)
    paged_users = user_repository.get_all(request_form, offset, per_page)

    pagination = Pagination(page=page, per_page=per_page, total=total, record_name='users',
                            format_total=True, format_number=True)
    return render_template('users.html', users=paged_users, page=page, per_page=per_page,
                           pagination=pagination, form=form)


@user_blueprint.route('/users/<username>')
def user_details(user_repository: UserRepository, username):
    try:
        user = user_repository.get(username)
    except UserNotFoundException:
        return not_found()

    return render_template('user_details.html', user=user)


def not_found():
    flash('User not found', 'error')
    return redirect(url_for('users.users'), 303)


class UserView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
