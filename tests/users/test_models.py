from instance.users.fakes import user1, user2
from tests.interfaces import test_basic


class UserTests(test_basic.BasicTests):

    def test_equals_with_non_user_should_return_false(self):
        self.assertFalse(user1 == object)

    def test_equals_with_other_user_should_return_false(self):
        self.assertFalse(user1 == user2)

    def test_equals_with_same_user_should_return_true(self):
        self.assertTrue(user1 == user1)
