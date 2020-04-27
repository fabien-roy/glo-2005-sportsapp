from instance.practice_centers.services import PracticeCenterPopulationService
from tests.practice_centers.mocks import practice_center_repository
from tests.interfaces.test_basic import BasicTests


class PracticeCenterPopulationServiceTests(BasicTests):

    def setUp(self):
        self.practice_center_population_service = PracticeCenterPopulationService(
            practice_center_repository)

    def test_db_populate_adds_fakes(self):
        self.practice_center_population_service.db_populate()
        self.assertTrue(practice_center_repository.add.called)
