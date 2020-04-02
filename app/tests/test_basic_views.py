import unittest

from app.tests import test_basic
from app.tests.practice_centers.fakes import get_practice_center, get_practice_centers_filtered, no_practice_center
from app.tests.practice_centers.mocks import practice_centers_repository
from app.tests.sports.fakes import get_sport, no_sport, get_sports_filtered
from app.tests.sports.mocks import sports_repository
from app.tests.users.fakes import user1, user2, user3, get_user, no_user
from app.tests.users.mocks import users_repository


class BasicViewTests(test_basic.BasicTests):
    def setUp(self):
        super().setUp()
        self.reset_mocks()
        self.add_sports()
        self.add_practice_centers()
        self.add_users()

    @staticmethod
    def reset_mocks():
        sports_repository.reset_mock()
        practice_centers_repository.reset_mock()
        users_repository.reset_mock()

    @staticmethod
    def add_sports():
        sports_repository.get.side_effect = get_sport
        sports_repository.get_all.side_effect = get_sports_filtered

    @staticmethod
    def remove_sports():
        sports_repository.get.side_effect = lambda sport_id: no_sport()
        sports_repository.get_all.side_effect = lambda form: []

    @staticmethod
    def add_practice_centers():
        practice_centers_repository.get.side_effect = get_practice_center
        practice_centers_repository.get_all.side_effect = get_practice_centers_filtered

    @staticmethod
    def remove_practice_centers():
        practice_centers_repository.get.side_effect = lambda practice_center_id: no_practice_center()
        practice_centers_repository.get_all.side_effect = lambda form: []

    @staticmethod
    def add_users():
        users_repository.get.side_effect = get_user
        users_repository.get_all.return_value = [user1, user2, user3]

    @staticmethod
    def remove_users():
        users_repository.get.side_effect = lambda username: no_user()
        users_repository.get_all.return_value = []


if __name__ == "__main__":
    unittest.main()