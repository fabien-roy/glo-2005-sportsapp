import unittest

from tests.equipments.fakes import equipment1, equipment2, equipment3
from tests.test_basic_views import BasicViewTests


class EquipmentsViewsTests(BasicViewTests):

    def test_equipments_with_no_equipment_should_display_no_equipment(self):
        self.remove_equipments()
        response = self.app.get('/equipments', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Equipments', response.data)
        self.assertNotIn(equipment1.name.encode(), response.data)
        self.assertNotIn(equipment2.name.encode(), response.data)
        self.assertNotIn(equipment3.name.encode(), response.data)

    def test_equipments_with_equipments_should_display_equipments(self):
        response = self.app.get('/equipments', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Equipments', response.data)
        self.assertIn(equipment1.name.encode(), response.data)
        self.assertIn(equipment2.name.encode(), response.data)
        self.assertIn(equipment3.name.encode(), response.data)

    def test_equipments_with_form_should_display_filtered_equipments(self):
        response = self.app.post('/equipments', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Equipments', response.data)
        self.assertIn(equipment1.name.encode(), response.data)
        self.assertNotIn(equipment2.name.encode(), response.data)
        self.assertNotIn(equipment3.name.encode(), response.data)

    def test_equipment_details_should_display_equipment_details(self):
        self.assert_item_details_are_displayed('/equipments', [
            (equipment1.id, equipment1.name),
            (equipment2.id, equipment2.name),
            (equipment3.id, equipment3.name),
        ])

    def test_equipment_details__without_equipment_should_respond_not_found(self):
        self.remove_equipments()
        self.assert_item_details_are_not_found('/equipments', [(equipment1.id, equipment1.name)])


if __name__ == "__main__":
    unittest.main()
