from instance.recommendations.services import RecommendationPopulationService
from tests.recommendations.mocks import recommendation_repository
from tests.interfaces.test_basic import BasicTests


class RecommendationPopulationServiceTests(BasicTests):

    def setUp(self):
        self.recommendation_population_service = RecommendationPopulationService(
            recommendation_repository)

    def test_db_populate_adds_fake_sports(self):
        self.recommendation_population_service.db_populate()
        self.assertTrue(recommendation_repository.add_to_sport.called)

    def test_db_populate_adds_fake_practice_centers(self):
        self.recommendation_population_service.db_populate()
        self.assertTrue(recommendation_repository.add_to_practice_center.called)
