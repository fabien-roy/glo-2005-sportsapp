import unittest

from tests.sports.fakes import sport1, sport3, sport2
from tests.test_basic_views import BasicViewTests


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
        self.assert_item_details_are_displayed('/sports', [
            (sport1.id, sport1.name),
            (sport2.id, sport2.name),
            (sport3.id, sport3.name),
        ])

    def test_sport_details__without_sport_should_respond_not_found(self):
        self.remove_sports()
        self.assert_item_details_are_not_found('/sports', [(sport1.id, sport1.name)])


if __name__ == "__main__":
    unittest.main()
