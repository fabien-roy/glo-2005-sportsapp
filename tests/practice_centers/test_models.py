from instance.practice_centers.fakes import center1, center2
from tests.interfaces import test_basic


class PracticeCenterTests(test_basic.BasicTests):

    def test_equals_with_non_practice_center_should_return_false(self):
        self.assertFalse(center1 == object)

    def test_equals_with_other_practice_center_should_return_false(self):
        self.assertFalse(center1 == center2)

    def test_equals_with_same_practice_center_should_return_true(self):
        self.assertTrue(center1 == center1)
