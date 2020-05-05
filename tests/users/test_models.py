from app.users.models import User
from tests.users.fakes import user1, user2
from tests.interfaces.test_basic import BasicTests


class UserTests(BasicTests):

    def test_equals_with_non_user_should_return_false(self):
        self.assertFalse(user1 == object)

    def test_equals_with_other_user_should_return_false(self):
        self.assertFalse(user1 == user2)

    def test_equals_with_same_user_should_return_true(self):
        self.assertTrue(user1 == user1)

    def test_is_authenticated_should_return_true(self):
        self.assertTrue(User.is_authenticated())

    def test_is_active_should_return_true(self):
        self.assertTrue(User.is_active())

    def test_is_anonymous_should_return_true(self):
        self.assertFalse(User.is_anonymous())
