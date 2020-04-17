import unittest

from app.announces.infrastructure.mysql.repositories import MySQLAnnounceRepository
from tests.equipments.fakes import equipment1, equipment2, equipment3
from tests.repositories.mysql_test_database import test_database
from tests.shops.fakes import shop3, shop2, shop1
from tests.test_basic_repositories import BasicRepositoryTests


class MySQLAnnounceRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLAnnounceRepository(test_database)

    def test_get_all_for_shop_should_without_shop_get_no_announce(self):
        self.recreate_database()
        announces = self.repository.get_all_for_shop(shop1.id)
        self.assertEqual(0, len(announces))
        announces = self.repository.get_all_for_shop(shop2.id)
        self.assertEqual(0, len(announces))
        announces = self.repository.get_all_for_shop(shop3.id)
        self.assertEqual(0, len(announces))

    def test_get_all_for_shop_should_get_shop_announces(self):
        announces = self.repository.get_all_for_shop(shop1.id)
        self.assertCountEqual(shop1.announces, announces)
        announces = self.repository.get_all_for_shop(shop2.id)
        self.assertCountEqual(shop2.announces, announces)
        announces = self.repository.get_all_for_shop(shop3.id)
        self.assertCountEqual(shop3.announces, announces)

    def test_get_all_for_equipment_should_without_equipment_get_no_announce(self):
        self.recreate_database()
        announces = self.repository.get_all_for_equipment(equipment1.id)
        self.assertEqual(0, len(announces))
        announces = self.repository.get_all_for_equipment(equipment2.id)
        self.assertEqual(0, len(announces))
        announces = self.repository.get_all_for_equipment(equipment3.id)
        self.assertEqual(0, len(announces))

    def test_get_all_for_equipment_should_get_equipment_announces(self):
        announces = self.repository.get_all_for_equipment(equipment1.id)
        self.assertCountEqual(equipment1.announces, announces)
        announces = self.repository.get_all_for_equipment(equipment2.id)
        self.assertCountEqual(equipment2.announces, announces)
        announces = self.repository.get_all_for_equipment(equipment3.id)
        self.assertCountEqual(equipment3.announces, announces)


if __name__ == "__main__":
    unittest.main()
