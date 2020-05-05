from app.admin.infrastructure.repositories import MySQLStatEventRepository
from tests.admin.fakes import user_login_event
from tests.interfaces.infrastructure.database import test_database
from tests.interfaces.infrastructure.test_repositories import RepositoryTests


class StatEventRepositoryTests(RepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLStatEventRepository(test_database)

    def test_get_all_with_no_event_should_get_no_event(self):
        self.recreate_database()
        events = self.repository.get_all()
        self.assertEqual(0, len(events))

    def test_get_all_should_get_events(self):
        events = self.repository.get_all()
        self.assertLess(0, len(events))

    def test_add_should_add_event(self):
        original_events = self.repository.get_all()
        self.repository.add(user_login_event)
        new_events = self.repository.get_all()
        self.assertLess(len(original_events), len(new_events))
