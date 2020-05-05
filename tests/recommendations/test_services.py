from app.recommendations.services import RecommendationService
from instance.practice_centers.fakes import center1
from instance.recommendations.services import RecommendationPopulationService
from instance.sports.fakes import sport1
from instance.users.fakes import user1
from tests.practice_centers.mocks import practice_center_repository
from tests.recommendations.forms import FakeAddRecommendationForm
from tests.recommendations.mocks import recommendation_repository
from tests.interfaces.test_basic import BasicTests
from tests.sports.mocks import sport_repository


class RecommendationServiceTests(BasicTests):

    def setUp(self):
        self.recommendation_service = RecommendationService(recommendation_repository)

    def test_add_to_sport_should_add_to_sport(self):
        form = FakeAddRecommendationForm(3, 'Comment')
        self.recommendation_service.add_to_sport(user1.username, sport1, form)
        recommendation_repository.add_to_sport.assert_called()

    def test_add_to_practice_center_should_add_to_practice_center(self):
        form = FakeAddRecommendationForm(3, 'Comment')
        self.recommendation_service.add_to_practice_center(user1.username, center1, form)
        recommendation_repository.add_to_practice_center.assert_called()


class RecommendationPopulationServiceTests(BasicTests):

    def setUp(self):
        self.recommendation_population_service = RecommendationPopulationService(
            recommendation_repository, sport_repository, practice_center_repository)

    def test_db_populate_adds_fake_sports(self):
        self.recommendation_population_service.db_populate()
        self.assertTrue(recommendation_repository.add_to_sport.called)

    def test_db_populate_adds_fake_practice_centers(self):
        self.recommendation_population_service.db_populate()
        self.assertTrue(recommendation_repository.add_to_practice_center.called)
