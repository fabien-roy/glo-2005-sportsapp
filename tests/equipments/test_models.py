from instance.equipments.fakes import equipment1, equipment2
from tests.interfaces.test_basic import BasicTests


class EquipmentTests(BasicTests):

    def test_equals_with_non_equipment_should_return_false(self):
        self.assertFalse(equipment1 == object)

    def test_equals_with_other_equipment_should_return_false(self):
        self.assertFalse(equipment1 == equipment2)

    def test_equals_with_same_equipment_should_return_true(self):
        self.assertTrue(equipment1 == equipment1)
