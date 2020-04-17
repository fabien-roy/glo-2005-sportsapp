from injector import Module

from app.climates.repositories import ClimateRepository
from tests.climates.mocks import climate_repository


class MockClimateModule(Module):
    def configure(self, binder):
        binder.bind(ClimateRepository, to=climate_repository)
