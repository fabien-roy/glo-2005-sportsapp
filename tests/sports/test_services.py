from instance.sports.services import SportPopulationService
from tests.sports.mocks import sport_repository
from tests.interfaces import test_basic


class SportPopulationServiceTests(test_basic.BasicTests):

    def setUp(self):
        self.sport_population_service = SportPopulationService(sport_repository)

    def test_db_populate_adds_fakes(self):
        self.sport_population_service.db_populate()
        assert sport_repository.add.called
