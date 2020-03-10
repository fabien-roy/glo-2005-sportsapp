import unittest

from app import app
from instance.db_create import db_create


class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['MYSQL_BD'] = 'test'

        self.app = app.test_client()

        db_create()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
