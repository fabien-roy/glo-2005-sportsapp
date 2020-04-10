import unittest

from app.tests.test_basic_views import BasicViewTests
from app.tests.users.fakes import user1, user2, user3


class UsersViewsTests(BasicViewTests):

    def test_users_with_no_sport_should_display_no_user(self):
        self.remove_users()
        response = self.app.get('/users', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Users', response.data)
        self.assertNotIn(user1.username.encode(), response.data)
        self.assertNotIn(user2.username.encode(), response.data)
        self.assertNotIn(user3.username.encode(), response.data)

    def test_users_with_users_should_display_users(self):
        response = self.app.get('/users', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Users', response.data)
        self.assertIn(user1.username.encode(), response.data)
        self.assertIn(user2.username.encode(), response.data)
        self.assertIn(user3.username.encode(), response.data)

    def test_users_with_form_should_display_filtered_users(self):
        response = self.app.post('/users', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Users', response.data)
        self.assertIn(user1.username.encode(), response.data)
        self.assertNotIn(user2.username.encode(), response.data)
        self.assertNotIn(user3.username.encode(), response.data)

    def test_user_details_should_display_user_details(self):
        response = self.app.get('/users/{}'.format(user1.username), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(user1.username.encode(), response.data)
        response = self.app.get('/users/{}'.format(user2.username), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(user2.username.encode(), response.data)
        response = self.app.get('/users/{}'.format(user3.username), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(user3.username.encode(), response.data)

    def test_user_details__without_user_should_respond_not_found(self):
        self.remove_users()
        response = self.app.get('/users/{}'.format(user1.username), follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)


if __name__ == "__main__":
    unittest.main()
