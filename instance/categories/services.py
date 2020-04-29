from injector import inject

from app.categories.repositories import CategoryRepository
from instance.categories.fakes import category1, category2, category3


class CategoryPopulationService:
    @inject
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def db_populate(self):
        self.category_repository.add(category1)
        self.category_repository.add(category2)
        self.category_repository.add(category3)
