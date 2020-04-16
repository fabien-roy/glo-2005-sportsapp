import unittest

from tests.practice_centers.fakes import center1, center2, center3
from tests.test_basic_views import BasicViewTests


class PracticeCentersViewsTests(BasicViewTests):

    def test_practice_centers_with_no_practice_center_should_display_no_practice_center(self):
        self.remove_practice_centers()
        response = self.app.get('/practice-centers', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Practice Centers', response.data)
        self.assertNotIn(center1.name.encode(), response.data)
        self.assertNotIn(center2.name.encode(), response.data)
        self.assertNotIn(center3.name.encode(), response.data)

    def test_practice_centers_with_practice_centers_should_display_practice_centers(self):
        response = self.app.get('/practice-centers', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Practice Centers', response.data)
        self.assertIn(center1.name.encode(), response.data)
        self.assertIn(center2.name.encode(), response.data)
        self.assertIn(center3.name.encode(), response.data)

    def test_practice_centers_with_form_should_display_filtered_practice_centers(self):
        response = self.app.post('/practice-centers', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Practice Centers', response.data)
        self.assertIn(center1.name.encode(), response.data)
        self.assertNotIn(center2.name.encode(), response.data)
        self.assertNotIn(center3.name.encode(), response.data)

    def test_practice_center_details_should_display_practice_center_details(self):
        self.assert_item_details_are_displayed('/practice-centers', [
            (center1.id, center1.name),
            (center2.id, center2.name),
            (center3.id, center3.name),
        ])

    def test_practice_center_details__without_practice_center_should_respond_not_found(self):
        self.remove_practice_centers()
        self.assert_item_details_are_not_found('/practice-centers', [(center1.id, center1.name)])


if __name__ == "__main__":
    unittest.main()
