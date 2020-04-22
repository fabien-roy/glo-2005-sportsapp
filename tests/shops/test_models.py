from instance.shops.fakes import shop1, shop2
from tests.interfaces.test_basic import BasicTests


class ShopTests(BasicTests):

    def test_equals_with_non_shop_should_return_false(self):
        self.assertFalse(shop1 == object)

    def test_equals_with_other_shop_should_return_false(self):
        self.assertFalse(shop1 == shop2)

    def test_equals_with_same_shop_should_return_true(self):
        self.assertTrue(shop1 == shop1)
