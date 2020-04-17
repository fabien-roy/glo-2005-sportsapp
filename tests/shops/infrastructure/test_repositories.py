import unittest

from app.shops.exceptions import ShopNotFoundException
from app.shops.infrastructure.repositories import MySQLShopRepository
from tests.announces.mocks import announce_repository
from tests.interfaces.infrastructure.database import test_database
from tests.interfaces.infrastructure.test_repositories import RepositoryTests
from tests.shops.fakes import shop1, shop2, shop3
from tests.shops.forms import FakeShopSearchForm


class ShopRepositoryTests(RepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLShopRepository(test_database, announce_repository)

    def test_get_with_no_shop_should_raise_shop_not_found_exception(self):
        self.recreate_database()
        self.assertRaises(ShopNotFoundException, self.repository.get, 1)

    def test_get_with_non_existent_shop_should_raise_shop_not_found_exception(self):
        self.assertRaises(ShopNotFoundException, self.repository.get, -1)

    def test_get_should_get_shop(self):
        shop = self.repository.get(shop1.id)
        self.assertEqual(shop1, shop)
        shop = self.repository.get(shop2.id)
        self.assertEqual(shop2, shop)
        shop = self.repository.get(shop3.id)
        self.assertEqual(shop3, shop)

    def test_get_should_get_shop_announces(self):
        shop = self.repository.get(shop1.id)
        self.assertCountEqual(shop1.announces, shop.announces)
        shop = self.repository.get(shop2.id)
        self.assertCountEqual(shop2.announces, shop.announces)
        shop = self.repository.get(shop3.id)
        self.assertCountEqual(shop3.announces, shop.announces)

    def test_get_all_with_no_shop_get_no_shop(self):
        self.recreate_database()
        shops = self.repository.get_all()
        self.assertEqual(0, len(shops))

    def test_get_all_get_shops(self):
        shops = self.repository.get_all()
        self.assertIn(shop1, shops)
        self.assertIn(shop2, shops)
        self.assertIn(shop3, shops)

    def test_get_all_with_all_filter_shops(self):
        form = FakeShopSearchForm(any_field=shop1.name)
        shops = self.repository.get_all(form)
        self.assertIn(shop1, shops)
        self.assertNotIn(shop2, shops)
        self.assertNotIn(shop3, shops)

    def test_get_all_with_name_filter_shops(self):
        form = FakeShopSearchForm(name=shop1.name)
        shops = self.repository.get_all(form)
        self.assertIn(shop1, shops)
        self.assertNotIn(shop2, shops)
        self.assertNotIn(shop3, shops)

    def test_get_all_with_email_filter_shops(self):
        print(shop3.email)
        form = FakeShopSearchForm(email=shop3.email)
        shops = self.repository.get_all(form)
        self.assertIn(shop3, shops)
        self.assertNotIn(shop1, shops)
        self.assertNotIn(shop2, shops)

    def test_get_all_with_web_site_filter_shops(self):
        form = FakeShopSearchForm(web_site=shop1.web_site)
        shops = self.repository.get_all(form)
        self.assertIn(shop1, shops)
        self.assertNotIn(shop2, shops)
        self.assertNotIn(shop3, shops)

    def test_get_all_with_phone_number_filter_shops(self):
        form = FakeShopSearchForm(phone_number=shop1.phone_number)
        shops = self.repository.get_all(form)
        self.assertIn(shop1, shops)
        self.assertNotIn(shop2, shops)
        self.assertNotIn(shop3, shops)


if __name__ == "__main__":
    unittest.main()
