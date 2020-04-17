from injector import Module

from app.recommendations.repositories import RecommendationRepository
from tests.recommendations.mocks import recommendation_repository


class MockRecommendationModule(Module):
    def configure(self, binder):
        binder.bind(RecommendationRepository, to=recommendation_repository)
