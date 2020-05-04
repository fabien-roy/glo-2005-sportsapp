from injector import Module

from app.recommendations.services import RecommendationService
from app.sports.repositories import SportRepository
from tests.recommendations.mocks import recommendation_service
from tests.sports.mocks import sport_repository


class MockSportModule(Module):
    def configure(self, binder):
        binder.bind(SportRepository, to=sport_repository)
        binder.bind(RecommendationService, to=recommendation_service)
