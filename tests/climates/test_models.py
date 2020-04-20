from instance.climates.fakes import climate1, climate2
from tests.interfaces import test_basic


class ClimateTests(test_basic.BasicTests):

    def test_equals_with_non_climate_should_return_false(self):
        self.assertFalse(climate1 == object)

    def test_equals_with_other_climate_should_return_false(self):
        self.assertFalse(climate1 == climate2)

    def test_equals_with_same_climate_should_return_true(self):
        self.assertTrue(climate1 == climate1)
