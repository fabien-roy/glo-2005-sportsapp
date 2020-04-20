from unittest.mock import Mock

from instance import PopulationService
from tests.interfaces import test_basic


class ShopPopulationServiceTests(test_basic.BasicTests):
    climate_population_service = Mock.mock()
    sport_population_service = Mock.mock()
    practice_center_population_service = Mock.mock()
    user_population_service = Mock.mock()
    recommendation_population_service = Mock.mock()
    shop_population_service = Mock.mock()
    equipment_population_service = Mock.mock()
    announce_population_service = Mock.mock()

    def setUp(self):
        self.population_service = PopulationService(
            self.climate_population_service,
            self.sport_population_service,
            self.practice_center_population_service,
            self.user_population_service,
            self.recommendation_population_service,
            self.shop_population_service,
            self.equipment_population_service,
            self.announce_population_service)

    def test_db_populate_adds_climates(self):
        self.population_service.db_populate()
        assert self.climate_population_service.db_populate.called
