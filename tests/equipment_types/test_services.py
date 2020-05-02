from instance.equipment_types.services import EquipmentTypePopulationService
from tests.interfaces.test_basic import BasicTests
from tests.equipment_types.mocks import equipment_type_repository


class EquipmentTypePopulationServiceTests(BasicTests):

    def setUp(self):
        self.equipment_type_population_service = EquipmentTypePopulationService(
            equipment_type_repository)

    def test_db_populate_adds_fakes(self):
        self.equipment_type_population_service.db_populate()
        self.assertTrue(equipment_type_repository.add.called)
