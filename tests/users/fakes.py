from app.users.exceptions import UserNotFoundException
from app.users.models import User

user1 = User(username='fabienroy28', email='fabienroy28@gmail.com', password='123456',
             first_name='Fabien', last_name='Roy', phone_number='123-456-7890')
user2 = User(username='mikaelvalliant', email='mikaelvalliant@gmail.com', password='123456',
             first_name='Mikael', last_name='Valliant')
user3 = User(username='getoutmyswamp', email='shrek@swamp.ca', first_name='Shrek',
             password='123456', phone_number='1 800-555-0101')


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
