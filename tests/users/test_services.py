from instance.users.services import UserPopulationService
from tests.users.mocks import user_repository
from tests.interfaces import test_basic


class UserPopulationServiceTests(test_basic.BasicTests):

    def setUp(self):
        self.user_population_service = UserPopulationService(user_repository)

    def test_db_populate_adds_fakes(self):
        self.user_population_service.db_populate()
        assert user_repository.add.called
