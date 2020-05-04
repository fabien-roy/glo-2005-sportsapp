from injector import Module

from app.sports.repositories import SportRepository
from tests.sports.mocks import sport_repository


class MockSportModule(Module):
    def configure(self, binder):
        binder.bind(SportRepository, to=sport_repository)
