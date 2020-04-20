from instance.recommendations.services import RecommendationPopulationService
from tests.recommendations.mocks import recommendation_repository
from tests.interfaces import test_basic


class RecommendationPopulationServiceTests(test_basic.BasicTests):

    def setUp(self):
        self.recommendation_population_service = RecommendationPopulationService(
            recommendation_repository)

    def test_db_populate_adds_fakes(self):
        self.recommendation_population_service.db_populate()
        assert recommendation_repository.add.called
