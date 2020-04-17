import inject

from app.users.repositories import UserRepository
from instance.users.fakes import user1, user2, user3
from instance.users.services import UserPopulationService


class MySQLUserPopulationService(UserPopulationService):
    user_repository = inject.attr(UserRepository)

    def db_populate(self):
        self.user_repository.add(user1)
        self.user_repository.add(user2)
        self.user_repository.add(user3)
