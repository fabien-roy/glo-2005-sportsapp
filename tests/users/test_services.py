from instance.users.services import UserPopulationService
from tests.users.mocks import user_repository
from tests.interfaces.test_basic import BasicTests


class UserPopulationServiceTests(BasicTests):

    def setUp(self):
        self.user_population_service = UserPopulationService(user_repository)

    def test_db_populate_adds_fakes(self):
        self.user_population_service.db_populate()
        self.assertTrue(user_repository.add.called)
