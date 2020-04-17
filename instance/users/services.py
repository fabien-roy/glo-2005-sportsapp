from injector import inject

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
