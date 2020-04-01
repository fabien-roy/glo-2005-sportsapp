from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.tests.fakes import sport1, sport2, sport3
from app.tests.test_basic_repositories import BasicRepositoryTests


class RecommendationsRepositoryTests(BasicRepositoryTests):

    def setUp(self):
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
        self.add_sports_with_recommendations()
        recommendations = self.repository.get_all_for_sport(sport1.id)
        self.assertCountEqual(sport1.recommendations, recommendations)
        recommendations = self.repository.get_all_for_sport(sport2.id)
        self.assertCountEqual(sport2.recommendations, recommendations)
        recommendations = self.repository.get_all_for_sport(sport3.id)
        self.assertCountEqual(sport3.recommendations, recommendations)
