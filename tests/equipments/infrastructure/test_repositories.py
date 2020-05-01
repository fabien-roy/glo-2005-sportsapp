from app.equipments.exceptions import EquipmentNotFoundException
from app.equipments.infrastructure.repositories import MySQLEquipmentRepository
from tests.announces.mocks import announce_repository
from tests.equipments.fakes import equipment1, equipment2, equipment3
from tests.manufacturers.fakes import manufacturer1
from tests.equipments.forms import FakeEquipmentSearchForm
from tests.interfaces.infrastructure.database import test_database
from tests.interfaces.infrastructure.test_repositories import RepositoryTests
from tests.sports.mocks import sport_repository


class EquipmentRepositoryTests(RepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLEquipmentRepository(test_database,
                                                   sport_repository,
                                                   announce_repository)

    def test_get_with_no_equipment_should_raise_equipment_not_found_exception(self):
        self.recreate_database()
        self.assertRaises(EquipmentNotFoundException, self.repository.get, 1)

    def test_get_with_non_existent_equipment_should_raise_equipment_not_found_exception(self):
        self.assertRaises(EquipmentNotFoundException, self.repository.get, -1)

    def test_get_should_get_equipment(self):
        equipment = self.repository.get(equipment1.id)
        self.assertEqual(equipment1, equipment)
        equipment = self.repository.get(equipment2.id)
        self.assertEqual(equipment2, equipment)
        equipment = self.repository.get(equipment3.id)
        self.assertEqual(equipment3, equipment)

    def test_get_should_get_manufacturer(self):
        equipment = self.repository.get(equipment1.id)
        self.assertEqual(equipment1.manufacturer_id, equipment.manufacturer_id)
        self.assertEqual(equipment1.manufacturer_name, equipment.manufacturer_name)
        equipment = self.repository.get(equipment2.id)
        self.assertEqual(equipment2.manufacturer_id, equipment.manufacturer_id)
        self.assertEqual(equipment2.manufacturer_name, equipment.manufacturer_name)
        equipment = self.repository.get(equipment3.id)
        self.assertEqual(equipment3.manufacturer_id, equipment.manufacturer_id)
        self.assertEqual(equipment3.manufacturer_name, equipment.manufacturer_name)

    def test_get_should_get_equipment_announces(self):
        equipment = self.repository.get(equipment1.id)
        self.assertCountEqual(equipment1.announces, equipment.announces)
        equipment = self.repository.get(equipment2.id)
        self.assertCountEqual(equipment2.announces, equipment.announces)
        equipment = self.repository.get(equipment3.id)
        self.assertCountEqual(equipment3.announces, equipment.announces)

    def test_get_all_with_no_equipment_get_no_equipment(self):
        self.recreate_database()
        equipments = self.repository.get_all()
        self.assertEqual(0, len(equipments))

    def test_get_all_get_equipments(self):
        equipments = self.repository.get_all()
        self.assertIn(equipment1, equipments)
        self.assertIn(equipment2, equipments)
        self.assertIn(equipment3, equipments)

    def test_get_all_with_all_filter_equipments(self):
        form = FakeEquipmentSearchForm(any_field=equipment1.name)
        equipments = self.repository.get_all(form)
        self.assertIn(equipment1, equipments)
        self.assertNotIn(equipment2, equipments)
        self.assertNotIn(equipment3, equipments)

    def test_get_all_with_manufacturer_filter_equipments(self):
        form = FakeEquipmentSearchForm(manufacturer=manufacturer1.name)
        equipments = self.repository.get_all(form)
        self.assertIn(equipment1, equipments)
        self.assertNotIn(equipment2, equipments)
        self.assertNotIn(equipment3, equipments)

    def test_get_all_with_name_filter_equipments(self):
        form = FakeEquipmentSearchForm(name=equipment1.name)
        equipments = self.repository.get_all(form)
        self.assertIn(equipment1, equipments)
        self.assertNotIn(equipment2, equipments)
        self.assertNotIn(equipment3, equipments)

    def test_get_all_with_category_filter_equipments(self):
        form = FakeEquipmentSearchForm(equipment_type=equipment1.type_name)
        equipments = self.repository.get_all(form)
        self.assertIn(equipment1, equipments)
        self.assertNotIn(equipment2, equipments)
        self.assertNotIn(equipment3, equipments)

    def test_get_all_with_description_filter_equipments(self):
        form = FakeEquipmentSearchForm(description=equipment1.description)
        equipments = self.repository.get_all(form)
        self.assertIn(equipment1, equipments)
        self.assertNotIn(equipment2, equipments)
        self.assertNotIn(equipment3, equipments)
