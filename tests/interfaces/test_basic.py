import unittest

from flask_injector import FlaskInjector

from app import app
from tests.bindings import configure_test_database, configure_mock_modules
from tests.users.fakes import user1


class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        FlaskInjector(app=app, modules=[configure_test_database, configure_mock_modules])

        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def logged_in_session(self):
        with self.app.session_transaction() as session:
            session["logged_in"] = True
            session["_user_id"] = user1.username

    def logged_out_session(self):
        with self.app.session_transaction() as session:
            session["logged_in"] = False
            session["_user_id"] = None

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
