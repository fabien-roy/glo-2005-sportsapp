from instance.equipments.services import EquipmentPopulationService
from tests.equipment_types.mocks import equipment_type_repository
from tests.equipments.mocks import equipment_repository
from tests.interfaces.test_basic import BasicTests
from tests.manufacturers.mocks import manufacturer_repository


class EquipmentPopulationServiceTests(BasicTests):

    def setUp(self):
        self.equipment_population_service = EquipmentPopulationService(equipment_repository,
                                                                       manufacturer_repository,
                                                                       equipment_type_repository)

    def test_db_populate_adds_fakes(self):
        self.equipment_population_service.db_populate()
        self.assertTrue(equipment_repository.add.called)
