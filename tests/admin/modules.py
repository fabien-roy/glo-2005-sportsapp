from injector import Module

from app.admin.repositories import StatEventRepository
from app.admin.services import StatService
from tests.admin.mocks import stat_event_repository, stat_service


class MockAdminModule(Module):
    def configure(self, binder):
        binder.bind(StatEventRepository, to=stat_event_repository)
        binder.bind(StatService, to=stat_service)
