import unittest

from app.tests.shops.fakes import shop1, shop2, shop3
from app.tests.test_basic_views import BasicViewTests


class ShopsViewsTests(BasicViewTests):

    def test_shops_with_no_shop_should_display_no_shop(self):
        self.remove_shops()
        response = self.app.get('/shops', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Shops', response.data)
        self.assertNotIn(shop1.name.encode(), response.data)
        self.assertNotIn(shop2.name.encode(), response.data)
        self.assertNotIn(shop3.name.encode(), response.data)

    def test_shops_with_shops_should_display_shops(self):
        response = self.app.get('/shops', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Shops', response.data)
        self.assertIn(shop1.name.encode(), response.data)
        self.assertIn(shop2.name.encode(), response.data)
        self.assertIn(shop3.name.encode(), response.data)

    def test_shops_with_form_should_display_filtered_shops(self):
        response = self.app.post('/shops', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Shops', response.data)
        self.assertIn(shop1.name.encode(), response.data)
        self.assertNotIn(shop2.name.encode(), response.data)
        self.assertNotIn(shop3.name.encode(), response.data)

    def test_shop_details_should_display_shop_details(self):
        response = self.app.get('/shops/{}'.format(shop1.id), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(shop1.name.encode(), response.data)
        response = self.app.get('/shops/{}'.format(shop2.id), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(shop2.name.encode(), response.data)
        response = self.app.get('/shops/{}'.format(shop3.id), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(shop3.name.encode(), response.data)

    def test_shop_details__without_shop_should_respond_not_found(self):
        self.remove_shops()
        response = self.app.get('/shops/{}'.format(shop1.id), follow_redirects=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)


if __name__ == "__main__":
    unittest.main()
