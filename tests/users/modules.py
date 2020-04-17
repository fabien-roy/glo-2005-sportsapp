from injector import Module

from app.users.repositories import UserRepository
from tests.users.mocks import user_repository


class MockUserModule(Module):
    def configure(self, binder):
        binder.bind(UserRepository, to=user_repository)
