import unittest

from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.tests.recommendations.mocks import recommendations_repository
from app.tests.test_basic_repositories import BasicRepositoryTests
from app.tests.users.fakes import user1, user2, user3
from app.users.exceptions import UserNotFoundException


class UsersRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLUsersRepository(recommendations_repository)

    def test_get_with_no_user_should_raise_user_not_found_exception(self):
        self.reset_repositories()
        self.assertRaises(UserNotFoundException, self.repository.get, 1)

    def test_get_with_non_existent_user_should_raise_user_not_found_exception(self):
        self.assertRaises(UserNotFoundException, self.repository.get, -1)

    def test_get_should_get_user(self):
        user = self.repository.get(user1.username)
        self.assertEqual(user1, user)
        user = self.repository.get(user2.username)
        self.assertEqual(user2, user)
        user = self.repository.get(user3.username)
        self.assertEqual(user3, user)

    def test_get_should_get_sports_recommendations(self):
        user = self.repository.get(user1.username)
        self.assertCountEqual(user1.sport_recommendations, user.sport_recommendations)
        user = self.repository.get(user2.username)
        self.assertCountEqual(user2.sport_recommendations, user.sport_recommendations)
        user = self.repository.get(user3.username)
        self.assertCountEqual(user3.sport_recommendations, user.sport_recommendations)

    def test_get_should_get_practice_centers_recommendations(self):
        user = self.repository.get(user1.username)
        self.assertCountEqual(user1.practice_center_recommendations, user.practice_center_recommendations)
        user = self.repository.get(user2.username)
        self.assertCountEqual(user2.practice_center_recommendations, user.practice_center_recommendations)
        user = self.repository.get(user3.username)
        self.assertCountEqual(user3.practice_center_recommendations, user.practice_center_recommendations)

    def test_get_all_with_no_user_center_get_no_user(self):
        self.reset_repositories()
        users = self.repository.get_all()
        self.assertEqual(0, len(users))

    def test_get_all_get_users(self):
        users = self.repository.get_all()
        self.assertIn(user1, users)
        self.assertIn(user2, users)
        self.assertIn(user3, users)


if __name__ == "__main__":
    unittest.main()