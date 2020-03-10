import unittest

from app.models import Sport
from app.sports.exceptions import SportNotFoundException
from app.tests import test_basic
from app.tests.mocks import sport_repository

sport1 = Sport(sport_id=1, name='Randonnee')
sport2 = Sport(sport_id=2, name='Escalade')
sport3 = Sport(sport_id=3, name='Natation')


def sports(sport_id):
    return {
        '1': sport1,
        '2': sport2,
        '3': sport3
    }[sport_id]


def no_sport():
    raise SportNotFoundException


def remove_sports():
    sport_repository.reset_mock()
    sport_repository.get.side_effect = lambda sport_id: no_sport()
    sport_repository.get_all.return_value = []


def add_sports():
    sport_repository.reset_mock()
    sport_repository.get.side_effect = sports
    sport_repository.get_all.return_value = [sport1, sport2, sport3]


class SportsTests(test_basic.BasicTests):

    def test_sports_with_no_sport_should_display_no_sport(self):
        remove_sports()
        response = self.app.get('/sports/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Sports', response.data)
        self.assertNotIn(b'Randonnee', response.data)
        self.assertNotIn(b'Escalade', response.data)
        self.assertNotIn(b'Natation', response.data)

    def test_sports_with_sports_should_display_sports(self):
        add_sports()
        response = self.app.get('/sports/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Sports', response.data)
        self.assertIn(b'Randonnee', response.data)
        self.assertIn(b'Escalade', response.data)
        self.assertIn(b'Natation', response.data)

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
