from app.equipments.exceptions import EquipmentNotFoundException
from app.repositories.mysql_equipment_repositories import MySQLEquipmentsRepository
from tests.equipments.fakes import equipment1, equipment2, equipment3
from tests.equipments.forms import FakeEquipmentsSearchForm
from tests.repositories.mysql_test_database import test_database
from tests.test_basic_repositories import BasicRepositoryTests


class EquipmentRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLEquipmentsRepository(test_database)

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
        form = FakeEquipmentsSearchForm(any_field=equipment1.name)
        equipments = self.repository.get_all(form)
        self.assertIn(equipment1, equipments)
        self.assertNotIn(equipment2, equipments)
        self.assertNotIn(equipment3, equipments)

    def test_get_all_with_name_filter_equipments(self):
        form = FakeEquipmentsSearchForm(name=equipment1.name)
        equipments = self.repository.get_all(form)
        self.assertIn(equipment1, equipments)
        self.assertNotIn(equipment2, equipments)
        self.assertNotIn(equipment3, equipments)

    def test_get_all_with_category_filter_equipments(self):
        form = FakeEquipmentsSearchForm(category=equipment1.category)
        equipments = self.repository.get_all(form)
        self.assertIn(equipment1, equipments)
        self.assertNotIn(equipment2, equipments)
        self.assertNotIn(equipment3, equipments)

    def test_get_all_with_description_filter_equipments(self):
        form = FakeEquipmentsSearchForm(description=equipment1.description)
        equipments = self.repository.get_all(form)
        self.assertIn(equipment1, equipments)
        self.assertNotIn(equipment2, equipments)
        self.assertNotIn(equipment3, equipments)
