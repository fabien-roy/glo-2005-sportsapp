import unittest
from unittest.mock import patch

from app.tests import test_basic
from app.tests.fakes import center1, center2, center3, no_practice_center, practice_centers
from app.tests.mocks import practice_center_repository


def remove_practice_centers():
    practice_center_repository.reset_mock()
    practice_center_repository.get.side_effect = lambda practice_center_id: no_practice_center()
    practice_center_repository.get_all.side_effect = lambda form: []


def add_practice_centers():
    practice_center_repository.reset_mock()
    practice_center_repository.get.side_effect = practice_centers
    practice_center_repository.get_all.side_effect = get_all_side_effect


def get_all_side_effect(form):
    if form is None:
        return [center1, center2, center3]
    else:
        return [center1]


class PracticeCentersViewsTests(test_basic.BasicTests):

    def test_practice_centers_with_no_practice_center_should_display_no_practice_center(self):
        remove_practice_centers()
        response = self.app.get('/practice-centers', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Practice Centers', response.data)
        self.assertNotIn(b'Mont-Orford National Park', response.data)
        self.assertNotIn(b'Parc des Montagnards', response.data)
        self.assertNotIn(b'Gault Nature Reserve of McGill University', response.data)

    def test_practice_centers_with_practice_centers_should_display_practice_centers(self):
        add_practice_centers()
        response = self.app.get('/practice-centers', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Practice Centers', response.data)
        self.assertIn(b'Mont-Orford National Park', response.data)
        self.assertIn(b'Parc des Montagnards', response.data)
        self.assertIn(b'Gault Nature Reserve of McGill University', response.data)

    @patch('app.practice_centers.views.search_form')
    def test_practice_centers_with_form_should_display_filtered_practice_centers(self, mock_search_form):
        add_practice_centers()
        response = self.app.post('/practice-centers', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Practice Centers', response.data)
        self.assertIn(b'Mont-Orford National Park', response.data)
        self.assertNotIn(b'Parc des Montagnards', response.data)
        self.assertNotIn(b'Gault Nature Reserve of McGill University', response.data)

    def test_practice_center_details_should_display_practice_center_details(self):
        add_practice_centers()
        response = self.app.get('/practice-centers/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mont-Orford National Park', response.data)
        response = self.app.get('/practice-centers/2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Parc des Montagnards', response.data)
        response = self.app.get('/practice-centers/3', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gault Nature Reserve of McGill University', response.data)

    def test_practice_center_details__without_practice_center_should_respond_not_found(self):
        remove_practice_centers()
        response = self.app.get('/practice-centers/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)


if __name__ == "__main__":
    unittest.main()
