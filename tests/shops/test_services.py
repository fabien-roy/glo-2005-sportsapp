from instance.shops.services import ShopPopulationService
from tests.shops.mocks import shop_repository
from tests.interfaces.test_basic import BasicTests


class ShopPopulationServiceTests(BasicTests):

    def setUp(self):
        self.shop_population_service = ShopPopulationService(shop_repository)

    def test_db_populate_adds_fakes(self):
        self.shop_population_service.db_populate()
        assert shop_repository.add.called
