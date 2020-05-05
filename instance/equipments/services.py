from injector import inject

from app.equipments.repositories import EquipmentRepository
from instance.equipments.fakes import equipment1, equipment2, equipment3


class EquipmentPopulationService:
    @inject
    def __init__(self, equipment_repository: EquipmentRepository):
        self.equipment_repository = equipment_repository

    def db_populate(self):
        self.equipment_repository.add(equipment1)
        self.equipment_repository.add(equipment2)
        self.equipment_repository.add(equipment3)
