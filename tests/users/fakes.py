from app.users.exceptions import UserNotFoundException
from instance.users.fakes import user1, user2, user3

user1.username = 'fabienroy28'
user2.username = 'mikaelvalliant'
user3.username = 'getoutmyswamp'


def get_user(username):
    return {
        'fabienroy28': user1,
        'mikaelvalliant': user2,
        'getoutmyswamp': user3
    }[username]


def no_user():
    raise UserNotFoundException


def get_users_filtered(form):
    if form is None:
        return [user1, user2, user3]

    return [user1]
