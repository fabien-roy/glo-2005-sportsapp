from tests.equipments.fakes import get_equipment, get_equipments_filtered, no_equipment
from tests.equipments.mocks import equipment_repository
from tests.interfaces.test_basic import BasicTests
from tests.practice_centers.fakes import get_practice_center, get_practice_centers_filtered, \
    no_practice_center
from tests.practice_centers.mocks import practice_center_repository
from tests.shops.mocks import shop_repository
from tests.sports.fakes import get_sport, no_sport, get_sports_filtered
from tests.sports.mocks import sport_repository
from tests.users.fakes import get_user, no_user, get_users_filtered
from tests.shops.fakes import get_shop, no_shop, get_shops_filtered
from tests.users.mocks import user_repository


class ViewTests(BasicTests):
    def setUp(self):
        super().setUp()
        self.reset_mocks()
        self.add_sports()
        self.add_practice_centers()
        self.add_users()
        self.add_shops()
        self.add_equipments()

    def get_path(self):
        pass

    @staticmethod
    def get_app_title():
        return 'SportsApp'

    def get_view_title(self):
        pass

    def request_get(self, reference=None):
        return self.app.get(self.request_path(reference), follow_redirects=True)

    def request_post(self, reference=None, data=None):
        return self.app.post(self.request_path(reference), follow_redirects=True, data=data)

    def request_path(self, reference=None):
        return self.get_path() if reference is None else f'{self.get_path()}/{reference}'

    @staticmethod
    def reset_mocks():
        sport_repository.reset_mock()
        practice_center_repository.reset_mock()
        user_repository.reset_mock()
        shop_repository.reset_mock()

    @staticmethod
    def add_sports():
        sport_repository.get.side_effect = get_sport
        sport_repository.get_all.side_effect = get_sports_filtered

    @staticmethod
    def remove_sports():
        sport_repository.get.side_effect = lambda sport_id: no_sport()
        sport_repository.get_all.side_effect = lambda form: []

    @staticmethod
    def add_practice_centers():
        practice_center_repository.get.side_effect = get_practice_center
        practice_center_repository.get_all.side_effect = get_practice_centers_filtered

    @staticmethod
    def remove_practice_centers():
        practice_center_repository.get.side_effect = \
            lambda practice_center_id: no_practice_center()
        practice_center_repository.get_all.side_effect = lambda form: []

    @staticmethod
    def add_users():
        user_repository.get.side_effect = get_user
        user_repository.get_all.side_effect = get_users_filtered

    @staticmethod
    def remove_users():
        user_repository.get.side_effect = lambda username: no_user()
        user_repository.get_all.side_effect = lambda form: []

    @staticmethod
    def add_shops():
        shop_repository.get.side_effect = get_shop
        shop_repository.get_all.side_effect = get_shops_filtered

    @staticmethod
    def remove_shops():
        shop_repository.get.side_effect = lambda shop_id: no_shop()
        shop_repository.get_all.side_effect = lambda form: []

    @staticmethod
    def add_equipments():
        equipment_repository.get.side_effect = get_equipment
        equipment_repository.get_all.side_effect = get_equipments_filtered

    @staticmethod
    def remove_equipments():
        equipment_repository.get.side_effect = lambda equipment_id: no_equipment()
        equipment_repository.get_all.side_effect = lambda form: []

    def assert_page_is_found(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.get_app_title().encode(), response.data)
        self.assertIn(self.get_view_title().encode(), response.data)

    def assert_page_is_not_found(self, response):
        self.assertEqual(response.status_code, 404)

    def assert_items_are_listed(self, response, tests):
        for expected_data in tests:
            self.assertIn(expected_data.encode(), response.data)

    def assert_items_are_not_listed(self, response, tests):
        for expected_data in tests:
            self.assertNotIn(expected_data.encode(), response.data)

    def assert_item_details_are_displayed(self, tests):
        for reference, item_details in tests:
            response = self.request_get(reference)
            self.assert_page_is_found(response)
            for item_detail in item_details:
                if item_detail is not None:
                    self.assertIn(item_detail.encode(), response.data)

    def assert_item_details_are_not_found(self, tests):
        for reference, expected_data in tests:
            response = self.request_get(reference)
            self.assert_page_is_not_found(response)
            self.assertNotIn(expected_data.encode(), response.data)

    @staticmethod
    def list_detail_list_names(detail_list):
        return list(map(lambda detail: detail.name, detail_list))
