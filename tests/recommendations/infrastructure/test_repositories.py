import unittest

from app.recommendations.infrastructure.repositories import MySQLRecommendationRepository
from tests.basics.infrastructure.test_basic_repositories import BasicRepositoryTests
from tests.practice_centers.fakes import center1, center2, center3
from tests.repositories.mysql_test_database import test_database
from tests.sports.fakes import sport1, sport2, sport3
from tests.users.fakes import user1, user2, user3


class RecommendationsRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLRecommendationRepository(test_database)

    def test_get_all_for_sport_without_sport_should_get_no_recommendation(self):
        self.recreate_database()
        recommendations = self.repository.get_all_for_sport(sport1.id)
        self.assertEqual(0, len(recommendations))
        recommendations = self.repository.get_all_for_sport(sport2.id)
        self.assertEqual(0, len(recommendations))
        recommendations = self.repository.get_all_for_sport(sport3.id)
        self.assertEqual(0, len(recommendations))

    def test_get_all_for_sport_should_get_sport_climates(self):
        recommendations = self.repository.get_all_for_sport(sport1.id)
        self.assertCountEqual(sport1.recommendations, recommendations)
        recommendations = self.repository.get_all_for_sport(sport2.id)
        self.assertCountEqual(sport2.recommendations, recommendations)
        recommendations = self.repository.get_all_for_sport(sport3.id)
        self.assertCountEqual(sport3.recommendations, recommendations)

    def test_get_all_for_practice_center_without_practice_center_should_get_no_recommendation(self):
        self.recreate_database()
        recommendations = self.repository.get_all_for_practice_center(center1.id)
        self.assertEqual(0, len(recommendations))
        recommendations = self.repository.get_all_for_practice_center(center2.id)
        self.assertEqual(0, len(recommendations))
        recommendations = self.repository.get_all_for_practice_center(center3.id)
        self.assertEqual(0, len(recommendations))

    def test_get_all_for_practice_center_should_get_practice_center_climates(self):
        recommendations = self.repository.get_all_for_practice_center(center1.id)
        self.assertCountEqual(center1.recommendations, recommendations)
        recommendations = self.repository.get_all_for_practice_center(center2.id)
        self.assertCountEqual(center2.recommendations, recommendations)
        recommendations = self.repository.get_all_for_practice_center(center3.id)
        self.assertCountEqual(center3.recommendations, recommendations)

    def test_get_all_for_sport_and_user_should_without_practice_center_get_no_recommendation(self):
        self.recreate_database()
        recommendations = self.repository.get_all_for_sport_and_user(user1.username)
        self.assertEqual(0, len(recommendations))
        recommendations = self.repository.get_all_for_sport_and_user(user2.username)
        self.assertEqual(0, len(recommendations))
        recommendations = self.repository.get_all_for_sport_and_user(user3.username)
        self.assertEqual(0, len(recommendations))

    def test_get_all_for_sport_and_user_should_get_practice_center_recommendations_of_user(self):
        recommendations = self.repository.get_all_for_sport_and_user(user1.username)
        self.assertCountEqual(user1.sport_recommendations, recommendations)
        recommendations = self.repository.get_all_for_sport_and_user(user2.username)
        self.assertCountEqual(user2.sport_recommendations, recommendations)
        recommendations = self.repository.get_all_for_sport_and_user(user3.username)
        self.assertCountEqual(user3.sport_recommendations, recommendations)

    def test_get_all_for_center_and_user_should_without_practice_center_get_no_recommendation(self):
        self.recreate_database()
        recommendations = self.repository.get_all_for_practice_center_and_user(user1.username)
        self.assertEqual(0, len(recommendations))
        recommendations = self.repository.get_all_for_practice_center_and_user(user2.username)
        self.assertEqual(0, len(recommendations))
        recommendations = self.repository.get_all_for_practice_center_and_user(user3.username)
        self.assertEqual(0, len(recommendations))

    def test_get_all_for_center_and_user_should_get_practice_center_recommendations_of_user(self):
        recommendations = self.repository.get_all_for_practice_center_and_user(user1.username)
        self.assertCountEqual(user1.practice_center_recommendations, recommendations)
        recommendations = self.repository.get_all_for_practice_center_and_user(user2.username)
        self.assertCountEqual(user2.practice_center_recommendations, recommendations)
        recommendations = self.repository.get_all_for_practice_center_and_user(user3.username)
        self.assertCountEqual(user3.practice_center_recommendations, recommendations)


if __name__ == "__main__":
    unittest.main()
