import unittest

from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.tests import test_basic
from app.tests.fakes import user2, \
    user1, user3, sport1, sport2, sport3, sport1_recommendation1_user1, sport2_recommendation1_user3, \
    sport2_recommendation2_user2, \
    sport3_recommendation1_user1, climate1, climate2, climate3, sport1_no_climates, sport2_no_climates, \
    sport3_no_climates, center1, center2, center3, center1_recommendation1_user1, center2_recommendation1_user1, \
    center2_recommendation2_user2, center3_recommendation1_user3, center3_recommendation2_user1
from app.tests.mocks import recommendations_repository
from app.tests.test_basic_repositories import BasicRepositoryTests
from app.users.exceptions import UserNotFoundException
from instance.db_create import db_create


def get_recommendations_for_sport_and_user(user_id):
    return get_user(user_id).sport_recommendations


def get_recommendations_for_practice_center_and_user(user_id):
    return get_user(user_id).practice_center_recommendations


def get_user(username):
    if username == user1.username:
        return user1
    if username == user2.username:
        return user2
    if username == user3.username:
        return user3


class UsersRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        recommendations_repository.get_all_for_sport_and_user.side_effect = get_recommendations_for_sport_and_user
        recommendations_repository.get_all_for_practice_center_and_user.side_effect = \
            get_recommendations_for_practice_center_and_user
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
