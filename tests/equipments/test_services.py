from instance.equipments.services import EquipmentPopulationService
from tests.equipments.mocks import equipment_repository
from tests.interfaces import test_basic


class EquipmentPopulationServiceTests(test_basic.BasicTests):

    def setUp(self):
        self.equipment_population_service = EquipmentPopulationService(equipment_repository)

    def test_db_populate_adds_fakes(self):
        self.equipment_population_service.db_populate()
        assert equipment_repository.add.called
