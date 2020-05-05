from injector import inject

from app.users.models import User
from app.users.repositories import UserRepository
from instance.resources.helpers import users_csv, read_elements


class UserPopulationService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def db_populate(self):
        print('Adding users (and encrypt passwords)...')
        for user in self.read_users():
            self.user_repository.add(user)
        print('Done adding users!')

    def read_users(self):
        return read_elements(users_csv(), self.build_user)

    @staticmethod
    def build_user(row):
        return User(username=row[0], password=row[1], email=row[2], first_name=row[3],
                    last_name=row[4], phone_number=row[5])
