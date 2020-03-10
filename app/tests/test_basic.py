import unittest

from app import app


# TODO : This test class can be used for login/register/logout

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
