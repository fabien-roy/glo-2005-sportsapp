import unittest

from app.tests.sports.fakes import sport1, sport3, sport2
from app.tests.test_basic_views import BasicViewTests


class SportsViewsTests(BasicViewTests):

    def test_sports_with_no_sport_should_display_no_sport(self):
        self.remove_sports()
        response = self.app.get('/sports', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Sports', response.data)
        self.assertNotIn(sport1.name.encode(), response.data)
        self.assertNotIn(sport2.name.encode(), response.data)
        self.assertNotIn(sport3.name.encode(), response.data)

    def test_sports_with_sports_should_display_sports(self):
        response = self.app.get('/sports', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Sports', response.data)
        self.assertIn(sport1.name.encode(), response.data)
        self.assertIn(sport2.name.encode(), response.data)
        self.assertIn(sport3.name.encode(), response.data)

    def test_sports_with_form_should_display_filtered_sports(self):
        response = self.app.post('/sports', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Sports', response.data)
        self.assertIn(sport1.name.encode(), response.data)
        self.assertNotIn(sport2.name.encode(), response.data)
        self.assertNotIn(sport3.name.encode(), response.data)

    def test_sport_details_should_display_sport_details(self):
        response = self.app.get('/sports/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(sport1.name.encode(), response.data)
        response = self.app.get('/sports/2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(sport2.name.encode(), response.data)
        response = self.app.get('/sports/3', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(sport3.name.encode(), response.data)

    def test_sport_details__without_sport_should_respond_not_found(self):
        self.remove_sports()
        response = self.app.get('/sports/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)


if __name__ == "__main__":
    unittest.main()
