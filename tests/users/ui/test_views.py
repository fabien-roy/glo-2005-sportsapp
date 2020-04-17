import unittest

from tests.test_basic_views import BasicViewTests
from tests.users.fakes import user1, user2, user3


class UsersViewsTests(BasicViewTests):

    def get_path(self):
        return '/users'

    def get_view_title(self):
        return 'Users'

    def test_users_with_no_sport_should_display_no_user(self):
        self.remove_users()
        response = self.request_get()
        self.assert_page_is_found(response)
        self.assert_items_are_not_listed(response, [user1.username, user2.username, user3.username])

    def test_users_with_users_should_display_users(self):
        response = self.request_get()
        self.assert_page_is_found(response)
        self.assert_items_are_listed(response, [user1.username, user2.username, user3.username])

    def test_users_with_form_should_display_filtered_users(self):
        response = self.request_post()
        self.assert_page_is_found(response)
        self.assert_items_are_listed(response, [user1.username])
        self.assert_items_are_not_listed(response, [user2.username, user3.username])

    def test_user_details_should_display_user_details(self):
        self.assert_item_details_are_displayed([
            (user1.username, self.get_user_details(user1)),
            (user2.username, self.get_user_details(user2)),
            (user3.username, self.get_user_details(user3))
        ])

    def test_user_details__without_user_should_respond_not_found(self):
        self.remove_users()
        self.assert_item_details_are_not_found([(user1.username, user1.username)])

    @staticmethod
    def get_user_details(user):
        return [user.username, user.first_name, user.last_name, user.email]


if __name__ == "__main__":
    unittest.main()
