from instance.announces.services import AnnouncePopulationService
from tests.announces.mocks import announce_repository
from tests.interfaces.test_basic import BasicTests


class AnnouncePopulationServiceTests(BasicTests):

    def setUp(self):
        self.announce_population_service = AnnouncePopulationService(announce_repository)

    def test_db_populate_adds_fakes(self):
        self.announce_population_service.db_populate()
        self.assertTrue(announce_repository.add.called)
