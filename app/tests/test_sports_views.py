import unittest

from app.tests import test_basic
from app.tests.sports.fakes import sports, no_sport, sport3, sport2, sport1
from app.tests.sports.mocks import sports_repository


def remove_sports():
    sports_repository.reset_mock()
    sports_repository.get.side_effect = lambda sport_id: no_sport()
    sports_repository.get_all.side_effect = lambda form: []


def add_sports():
    sports_repository.reset_mock()
    sports_repository.get.side_effect = sports
    sports_repository.get_all.side_effect = get_all_side_effect


def get_all_side_effect(form):
    if form is None:
        return [sport1, sport2, sport3]
    else:
        return [sport1]


class SportsViewsTests(test_basic.BasicTests):

    def test_sports_with_no_sport_should_display_no_sport(self):
        remove_sports()
        response = self.app.get('/sports', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Sports', response.data)
        self.assertNotIn(b'Randonnee', response.data)
        self.assertNotIn(b'Escalade', response.data)
        self.assertNotIn(b'Natation', response.data)

    def test_sports_with_sports_should_display_sports(self):
        add_sports()
        response = self.app.get('/sports', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Sports', response.data)
        self.assertIn(b'Randonnee', response.data)
        self.assertIn(b'Escalade', response.data)
        self.assertIn(b'Natation', response.data)

    def test_sports_with_form_should_display_filtered_sports(self):
        add_sports()
        response = self.app.post('/sports', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Sports', response.data)
        self.assertIn(b'Randonnee', response.data)
        self.assertNotIn(b'Escalade', response.data)
        self.assertNotIn(b'Natation', response.data)

    def test_sport_details_should_display_sport_details(self):
        add_sports()
        response = self.app.get('/sports/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Randonnee', response.data)
        response = self.app.get('/sports/2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Escalade', response.data)
        response = self.app.get('/sports/3', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Natation', response.data)

    def test_sport_details__without_sport_should_respond_not_found(self):
        remove_sports()
        response = self.app.get('/sports/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)


if __name__ == "__main__":
    unittest.main()
