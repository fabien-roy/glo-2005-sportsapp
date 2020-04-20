from instance.climates.services import ClimatePopulationService
from tests.climates.mocks import climate_repository
from tests.interfaces import test_basic


class ClimatePopulationServiceTests(test_basic.BasicTests):

    def setUp(self):
        self.climate_population_service = ClimatePopulationService(climate_repository)

    def test_db_populate_adds_fakes(self):
        self.climate_population_service.db_populate()
        assert climate_repository.add.called
