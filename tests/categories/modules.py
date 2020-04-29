from injector import Module

from app.categories.repositories import CategoryRepository
from tests.categories.mocks import category_repository


class MockCategoryModule(Module):
    def configure(self, binder):
        binder.bind(CategoryRepository, to=category_repository)
