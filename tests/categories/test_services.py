from instance.categories.services import CategoryPopulationService
from tests.interfaces.test_basic import BasicTests
from tests.categories.mocks import category_repository


class CategoryPopulationServiceTests(BasicTests):

    def setUp(self):
        self.category_population_service = CategoryPopulationService(
            category_repository)

    def test_db_populate_adds_fakes(self):
        self.category_population_service.db_populate()
        self.assertTrue(category_repository.add.called)
