from instance.announces.services import AnnouncePopulationService
from tests.announces.mocks import announce_repository
from tests.equipments.mocks import equipment_repository
from tests.interfaces.test_basic import BasicTests
from tests.shops.mocks import shop_repository


class AnnouncePopulationServiceTests(BasicTests):

    def setUp(self):
        self.announce_population_service = AnnouncePopulationService(announce_repository,
                                                                     shop_repository,
                                                                     equipment_repository)

    def test_db_populate_adds_fakes(self):
        self.announce_population_service.db_populate()
        self.assertTrue(announce_repository.add.called)
