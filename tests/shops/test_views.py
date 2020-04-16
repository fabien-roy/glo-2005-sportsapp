import unittest

from tests.shops.fakes import shop1, shop2, shop3
from tests.test_basic_views import BasicViewTests


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
        self.assert_item_details_are_displayed('/shops', [
            (shop1.id, shop1.name),
            (shop2.id, shop2.name),
            (shop3.id, shop3.name)
        ])

    def test_shop_details__without_shop_should_respond_not_found(self):
        self.remove_shops()
        self.assert_item_details_are_not_found('/shops', [(shop1.id, shop1.name)])


if __name__ == "__main__":
    unittest.main()
