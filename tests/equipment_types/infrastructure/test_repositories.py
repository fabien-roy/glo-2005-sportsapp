from app.equipment_types.infrastructure.repositories import MySQLEquipmentTypeRepository
from tests.interfaces.infrastructure.database import test_database
from tests.interfaces.infrastructure.test_repositories import RepositoryTests
from tests.sports.fakes import sport1, sport2, sport3, get_equipment_types_for_sport


class EquipmentTypeRepositoryTests(RepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLEquipmentTypeRepository(test_database)

    def test_get_all_for_sport_type_should_get_equipment_types_for_sport(self):
        sports = self.repository.get_all_for_sport(sport1.id)
        self.assertCountEqual(get_equipment_types_for_sport(sport1.id), sports)
        sports = self.repository.get_all_for_sport(sport2.id)
        self.assertCountEqual(get_equipment_types_for_sport(sport2.id), sports)
        sports = self.repository.get_all_for_sport(sport3.id)
        self.assertCountEqual(get_equipment_types_for_sport(sport3.id), sports)
