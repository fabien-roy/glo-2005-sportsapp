import unittest

from tests import test_basic
from tests.equipments.fakes import get_equipment, get_equipments_filtered, no_equipment
from tests.equipments.mocks import equipments_repository
from tests.practice_centers.fakes import get_practice_center, get_practice_centers_filtered, \
    no_practice_center
from tests.practice_centers.mocks import practice_centers_repository
from tests.sports.fakes import get_sport, no_sport, get_sports_filtered
from tests.sports.mocks import sports_repository
from tests.users.fakes import get_user, no_user, get_users_filtered
from tests.users.mocks import users_repository
from tests.shops.mocks import shops_repository
from tests.shops.fakes import get_shop, no_shop, get_shops_filtered


class BasicViewTests(test_basic.BasicTests):
    def setUp(self):
        super().setUp()
        self.reset_mocks()
        self.add_sports()
        self.add_practice_centers()
        self.add_users()
        self.add_shops()
        self.add_equipments()

    @staticmethod
    def reset_mocks():
        sports_repository.reset_mock()
        practice_centers_repository.reset_mock()
        users_repository.reset_mock()
        shops_repository.reset_mock()

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
        practice_centers_repository.get.side_effect = \
            lambda practice_center_id: no_practice_center()
        practice_centers_repository.get_all.side_effect = lambda form: []

    @staticmethod
    def add_users():
        users_repository.get.side_effect = get_user
        users_repository.get_all.side_effect = get_users_filtered

    @staticmethod
    def remove_users():
        users_repository.get.side_effect = lambda username: no_user()
        users_repository.get_all.side_effect = lambda form: []

    @staticmethod
    def add_shops():
        shops_repository.get.side_effect = get_shop
        shops_repository.get_all.side_effect = get_shops_filtered

    @staticmethod
    def remove_shops():
        shops_repository.get.side_effect = lambda shop_id: no_shop()
        shops_repository.get_all.side_effect = lambda form: []

    @staticmethod
    def add_equipments():
        equipments_repository.get.side_effect = get_equipment
        equipments_repository.get_all.side_effect = get_equipments_filtered

    @staticmethod
    def remove_equipments():
        equipments_repository.get.side_effect = lambda equipment_id: no_equipment()
        equipments_repository.get_all.side_effect = lambda form: []


if __name__ == "__main__":
    unittest.main()
