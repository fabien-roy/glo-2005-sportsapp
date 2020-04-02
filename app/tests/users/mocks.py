from unittest import mock

from app.tests.users.fakes import user1, user2, user3

users_repository = mock.Mock()


def get_user(username):
    if username == user1.username:
        return user1
    if username == user2.username:
        return user2
    if username == user3.username:
        return user3
