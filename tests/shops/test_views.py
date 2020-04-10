import unittest

from tests.test_basic_views import BasicViewTests


class ShopsViewsTests(BasicViewTests):

    def test_shops_with_no_shop_should_display_no_shop(self):
        self.remove_shops()
        response = self.app.get('/shops', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Shops', response.data)
        self.assertNotIn(b'MEC Quebec City', response.data)
        self.assertNotIn(b'Sportium', response.data)
        self.assertNotIn(b'Au Grand Bazar La Source Du Sport', response.data)

    def test_shops_with_shops_should_display_shops(self):
        response = self.app.get('/shops', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Shops', response.data)
        self.assertIn(b'MEC Quebec City', response.data)
        self.assertIn(b'Sportium', response.data)
        self.assertIn(b'Au Grand Bazar La Source Du Sport', response.data)

    def test_shops_with_form_should_display_filtered_shops(self):
        response = self.app.post('/shops', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Shops', response.data)
        self.assertIn(b'MEC Quebec City', response.data)
        self.assertNotIn(b'Sportium', response.data)
        self.assertNotIn(b'Au Grand Bazar La Source Du Sport', response.data)

    def test_shop_details_should_display_shop_details(self):
        response = self.app.get('/shops/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MEC Quebec City', response.data)
        response = self.app.get('/shops/2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sportium', response.data)
        response = self.app.get('/shops/3', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Au Grand Bazar La Source Du Sport', response.data)

    def test_shop_details__without_shop_should_respond_not_found(self):
        self.remove_shops()
        response = self.app.get('/shops/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)


if __name__ == "__main__":
    unittest.main()
