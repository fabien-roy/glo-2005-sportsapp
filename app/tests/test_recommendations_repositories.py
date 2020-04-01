import unittest

from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.tests.fakes import sport1, sport2, sport3, center1, center2, center3
from app.tests.test_basic_repositories import BasicRepositoryTests


class RecommendationsRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        self.reset_repositories()
        self.add_users()
        self.add_climates()
        self.add_sports()
        self.add_practice_centers()
        self.add_sport_recommendations()
        self.add_practice_center_recommendations()
        self.repository = MySQLRecommendationsRepository()

    def test_get_all_for_sport_should_without_sport_get_no_recommendation(self):
        self.reset_repositories()
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

    def test_get_all_for_practice_center_should_without_practice_center_get_no_recommendation(self):
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


if __name__ == "__main__":
    unittest.main()
