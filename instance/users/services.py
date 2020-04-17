from app.users.repositories import UserRepository
from instance import injector
from instance.users.fakes import user1, user2, user3

user_repository = injector.get(UserRepository)


def db_populate_with_users():
    user_repository.add(user1)
    user_repository.add(user2)
    user_repository.add(user3)
