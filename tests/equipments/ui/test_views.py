import unittest

from app.equipments.ui.views import EquipmentView
from tests.equipments.fakes import equipment1, equipment2, equipment3
from tests.equipments.mocks import equipment_repository
from tests.interfaces.ui.test_views import ViewTests


class EquipmentViewTests(ViewTests):

    def test_construct_should_inject_repository(self):
        view = EquipmentView(equipment_repository)
        self.assertEquals(equipment_repository, view.equipment_repository)

    def get_path(self):
        return '/equipments'

    def get_view_title(self):
        return 'Equipments'

    def test_equipments_with_no_equipment_should_display_no_equipment(self):
        self.remove_equipments()
        response = self.request_get()
        self.assert_page_is_found(response)
        self.assert_items_are_not_listed(response, [equipment1.name, equipment2.name,
                                                    equipment3.name])

    def test_equipments_with_equipments_should_display_equipments(self):
        response = self.request_get()
        self.assert_page_is_found(response)
        self.assert_items_are_listed(response, [equipment1.name, equipment2.name, equipment3.name])

    def test_equipments_with_form_should_display_filtered_equipments(self):
        response = self.request_post()
        self.assert_page_is_found(response)
        self.assert_items_are_listed(response, [equipment1.name])
        self.assert_items_are_not_listed(response, [equipment2.name, equipment3.name])

    def test_equipment_details_should_display_equipment_details(self):
        self.assert_item_details_are_displayed([
            (equipment1.id, self.get_equipment_details(equipment1)),
            (equipment2.id, self.get_equipment_details(equipment2)),
            (equipment3.id, self.get_equipment_details(equipment3))
        ])

    def test_equipment_details__without_equipment_should_respond_not_found(self):
        self.remove_equipments()
        self.assert_item_details_are_not_found([(equipment1.id, equipment1.name)])

    def test_equipment_details_should_display_announces(self):
        self.assert_item_details_are_displayed([
            (equipment1.id, self.get_announces_details(equipment1)),
            (equipment2.id, self.get_announces_details(equipment2)),
            (equipment3.id, self.get_announces_details(equipment3))
        ])

    @staticmethod
    def get_equipment_details(equipment):
        return [equipment.name, equipment.category, equipment.description]

    @staticmethod
    def get_announces_details(equipment):
        details = []
        for announce in equipment.announces:
            details += [announce.shop_name, announce.state]
        return details


if __name__ == "__main__":
    unittest.main()
