from injector import Module

from app.practice_centers.repositories import PracticeCenterRepository
from tests.practice_centers.mocks import practice_center_repository


class MockPracticeCenterModule(Module):
    def configure(self, binder):
        binder.bind(PracticeCenterRepository, to=practice_center_repository)
