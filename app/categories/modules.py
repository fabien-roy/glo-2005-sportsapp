from injector import Module

from app.categories.infrastructure.repositories import MySQLCategoryRepository
from app.categories.repositories import CategoryRepository


class CategoryModule(Module):
    def configure(self, binder):
        binder.bind(CategoryRepository, to=MySQLCategoryRepository)
