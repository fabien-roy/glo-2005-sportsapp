from instance.manufacturers.services import ManufacturerPopulationService
from tests.interfaces.test_basic import BasicTests
from tests.manufacturers.mocks import manufacturer_repository


class ManufacturerPopulationServiceTests(BasicTests):

    def setUp(self):
        self.manufacturer_population_service = ManufacturerPopulationService(
            manufacturer_repository)

    def test_db_populate_adds_fakes(self):
        self.manufacturer_population_service.db_populate()
        self.assertTrue(manufacturer_repository.add.called)
