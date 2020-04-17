from injector import Module

from app.announces.repositories import AnnounceRepository
from tests.announces.mocks import announce_repository


class MockAnnounceModule(Module):
    def configure(self, binder):
        binder.bind(AnnounceRepository, to=announce_repository)
