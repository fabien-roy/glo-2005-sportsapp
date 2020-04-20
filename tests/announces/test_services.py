from instance.announces.services import AnnouncePopulationService
from tests.announces.mocks import announce_repository
from tests.interfaces import test_basic


class AnnouncePopulationServiceTests(test_basic.BasicTests):

    def setUp(self):
        self.announce_population_service = AnnouncePopulationService(announce_repository)

    def test_db_populate_adds_fakes(self):
        self.announce_population_service.db_populate()
        assert announce_repository.add.called
