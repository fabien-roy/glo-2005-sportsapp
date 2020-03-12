import unittest

from app.repositories.mysql_climate_repositories import MySQLClimateRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCenterRepository
from app.repositories.mysql_sport_repositories import MySQLSportRepository, MySQLSportClimateRepository
from app.repositories.mysql_user_repositories import MySQLUserRepository
from app.tests import test_basic
from app.tests.fakes import user2, \
    user1, user3
from app.users.exceptions import UserNotFoundException
from instance.db_create import db_create

sport_repository = MySQLSportRepository()
practice_center_repository = MySQLPracticeCenterRepository()
climate_repository = MySQLClimateRepository()
sport_climate_repository = MySQLSportClimateRepository()
user_repository = MySQLUserRepository()


def reset_repositories():
    db_create()

def add_users():
    reset_repositories()
    user_repository.add(user1)
    user_repository.add(user2)
    user_repository.add(user3)


class UsersRepositoryTests(test_basic.BasicTests):

    def test_get_with_no_user_should_raise_user_not_found_exception(self):
        reset_repositories()
        self.assertRaises(UserNotFoundException, user_repository.get, 1)

    def test_get_with_non_existent_user_should_raise_user_not_found_exception(self):
        add_users()
        self.assertRaises(UserNotFoundException, user_repository.get, -1)

    def test_get_should_get_user(self):
        add_users()
        user = user_repository.get(user1.username)
        self.assertEqual(user1, user)
        user = user_repository.get(user2.username)
        self.assertEqual(user2, user)
        user = user_repository.get(user3.username)
        self.assertEqual(user3, user)

    def test_get_all_with_no_user_center_get_no_user(self):
        reset_repositories()
        users = user_repository.get_all()
        self.assertEqual(0, len(users))

    def test_get_all_get_users(self):
        add_users()
        users = user_repository.get_all()
        self.assertIn(user1, users)
        self.assertIn(user2, users)
        self.assertIn(user3, users)


if __name__ == "__main__":
    unittest.main()
