from tests.announces.fakes import shop1_equipment1_announce1, shop1_equipment2_announce1
from tests.interfaces.test_basic import BasicTests


class AnnounceTests(BasicTests):

    def test_equals_with_non_announce_should_return_false(self):
        self.assertFalse(shop1_equipment1_announce1 == object)

    def test_equals_with_other_announce_should_return_false(self):
        self.assertFalse(shop1_equipment1_announce1 == shop1_equipment2_announce1)

    def test_equals_with_same_announce_should_return_true(self):
        self.assertTrue(shop1_equipment1_announce1 == shop1_equipment1_announce1)
