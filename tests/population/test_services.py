from unittest import mock

from instance import PopulationService
from tests.interfaces.test_basic import BasicTests


class ShopPopulationServiceTests(BasicTests):
    climate_population_service = mock.Mock()
    sport_population_service = mock.Mock()
    practice_center_population_service = mock.Mock()
    user_population_service = mock.Mock()
    recommendation_population_service = mock.Mock()
    shop_population_service = mock.Mock()
    manufacturer_population_service = mock.Mock()
    category_population_service = mock.Mock()
    equipment_population_service = mock.Mock()
    announce_population_service = mock.Mock()

    def setUp(self):
        self.population_service = PopulationService(self.user_population_service,
                                                    self.shop_population_service,
                                                    self.manufacturer_population_service,
                                                    self.category_population_service,
                                                    self.equipment_population_service,
                                                    self.announce_population_service,
                                                    self.climate_population_service,
                                                    self.sport_population_service,
                                                    self.practice_center_population_service,
                                                    self.recommendation_population_service)

        self.population_service.db_populate()

    def test_db_populate_adds_climates(self):
        self.assertTrue(self.climate_population_service.db_populate.called)

    def test_db_populate_adds_sports(self):
        self.assertTrue(self.sport_population_service.db_populate.called)

    def test_db_populate_adds_practice_centers(self):
        self.assertTrue(self.practice_center_population_service.db_populate.called)

    def test_db_populate_adds_users(self):
        self.assertTrue(self.user_population_service.db_populate.called)

    def test_db_populate_adds_recommendations(self):
        self.assertTrue(self.recommendation_population_service.db_populate.called)

    def test_db_populate_adds_shops(self):
        self.assertTrue(self.shop_population_service.db_populate.called)

    def test_db_populate_adds_manufacturers(self):
        self.assertTrue(self.manufacturer_population_service.db_populate.called)

    def test_db_populate_adds_categories(self):
        self.assertTrue(self.category_population_service.db_populate.called)

    def test_db_populate_adds_equipments(self):
        self.assertTrue(self.equipment_population_service.db_populate.called)

    def test_db_populate_adds_announces(self):
        self.assertTrue(self.announce_population_service.db_populate.called)
