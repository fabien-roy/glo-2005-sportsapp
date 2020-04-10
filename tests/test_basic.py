import unittest

from flask_injector import FlaskInjector

from app import app
from tests.bindings import configure


class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['MYSQL_USER'] = 'travis'
        app.config['MYSQL_PASSWORD'] = ''
        app.config['MYSQL_BD'] = 'sportsapp_test'

        FlaskInjector(app=app, modules=[configure])

        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
