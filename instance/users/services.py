from injector import inject

from app.users.models import User
from app.users.repositories import UserRepository
from instance.users.fakes import user1, user2, user3


class UserPopulationService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def db_populate(self):
        self.user_repository.add(user1)
        self.user_repository.add(user2)
        self.user_repository.add(user3)
        # TODO : Remove
        for i in range(10):
            self.user_repository.add(self.build_user(i))

    @staticmethod
    def build_user(i):
        username = f'user{i}'
        email = f'{username}@email.com'
        return User(username, email, password='123456')
