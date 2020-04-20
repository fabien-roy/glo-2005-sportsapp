from instance.sports.fakes import sport1, sport2
from tests.interfaces import test_basic


class TestSport(test_basic.BasicTests):

    def test_equals_with_non_sport_should_return_false(self):
        self.assertFalse(sport1 == object)

    def test_equals_with_other_sport_should_return_false(self):
        self.assertFalse(sport1 == sport2)

    def test_equals_with_same_sport_should_return_true(self):
        self.assertTrue(sport1 == sport1)
