from instance.practice_centers.services import PracticeCenterPopulationService
from tests.practice_centers.mocks import practice_center_repository
from tests.interfaces import test_basic


class PracticeCenterPopulationServiceTests(test_basic.BasicTests):

    def setUp(self):
        self.practice_center_population_service = PracticeCenterPopulationService(
            practice_center_repository)

    def test_db_populate_adds_fakes(self):
        self.practice_center_population_service.db_populate()
        assert practice_center_repository.add.called
