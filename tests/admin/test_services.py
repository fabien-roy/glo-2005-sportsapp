from app.admin.services import StatService
from tests.admin.fakes import recommendation_add_event, user_register_event, user_login_event
from tests.admin.mocks import stat_event_repository
from tests.interfaces.test_basic import BasicTests


class StatServiceTests(BasicTests):

    def setUp(self):
        self.stat_service = StatService(stat_event_repository)

    def test_get_all_stat_events_sums_with_no_event_should_return_zeros(self):
        stat_event_repository.get_all.return_value = []
        event_sums = self.stat_service.get_all_stat_event_sums()
        self.assert_contains(event_sums, 0, 0, 0)

    def test_get_all_stat_events_sums_with_events_should_return_one_of_each_event(self):
        for i in range(0, 2):
            for j in range(0, 2):
                for k in range(0, 2):
                    stat_event_repository.get_all.return_value = self.build_events(i, j, k)
                    event_sums = self.stat_service.get_all_stat_event_sums()
                    self.assert_contains(event_sums, i, j, k)

    def build_events(self, user_logins, user_registers, recommendation_adds):
        events = self.build_events_for_amount(user_login_event, user_logins)
        events.extend(self.build_events_for_amount(user_register_event, user_registers))
        events.extend(self.build_events_for_amount(recommendation_add_event, recommendation_adds))
        return events

    @staticmethod
    def build_events_for_amount(event, amount):
        return [event] * amount

    def test_add_user_login_should_add_event(self):
        self.stat_service.add_user_login()
        stat_event_repository.add.assert_called()

    def assert_contains(self, event_sums, user_logins, user_registers, recommendation_adds):
        self.assertEqual(3, len(event_sums))
        self.assertEqual(event_sums['USER_LOGIN'], user_logins)
        self.assertEqual(event_sums['USER_REGISTER'], user_registers)
        self.assertEqual(event_sums['RECOMMENDATION_ADD'], recommendation_adds)
