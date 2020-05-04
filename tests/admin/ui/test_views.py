from app.admin.ui.views import AdminView
from tests.admin.mocks import stat_service
from tests.interfaces.ui.test_views import ViewTests


class AdminViewTests(ViewTests):

    event_type_names = ['User login', 'User register', 'Recommendation add']

    def test_construct_should_inject_repository(self):
        view = AdminView(stat_service)
        self.assertEqual(stat_service, view.stat_service)

    def get_path(self):
        return '/admin/stats'

    def get_view_title(self):
        return 'Statistics'

    def test_stats_with_no_events_should_display_no_event(self):
        self.remove_events()
        response = self.request_get()
        self.assert_page_is_found(response)
        self.assert_items_are_listed(response, self.event_type_names)

    def test_stats_with_events_should_display_events(self):
        response = self.request_get()
        self.assert_page_is_found(response)
        self.assert_items_are_listed(response, self.event_type_names)
