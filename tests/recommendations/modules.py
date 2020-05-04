from injector import Module

from app.recommendations.repositories import RecommendationRepository
from app.recommendations.services import RecommendationService
from tests.recommendations.mocks import recommendation_repository, recommendation_service


class MockRecommendationModule(Module):
    def configure(self, binder):
        binder.bind(RecommendationRepository, to=recommendation_repository)
        binder.bind(RecommendationService, to=recommendation_service)
