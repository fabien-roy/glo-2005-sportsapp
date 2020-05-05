from injector import inject

from app.equipment_types.repositories import EquipmentTypeRepository
from app.equipments.models import Equipment
from app.equipments.repositories import EquipmentRepository
from app.manufacturers.repositories import ManufacturerRepository
from instance.resources.helpers import read_elements, equipments_csv


class EquipmentPopulationService:
    @inject
    def __init__(self, equipment_repository: EquipmentRepository,
                 manufacturer_repository: ManufacturerRepository,
                 equipment_type_repository: EquipmentTypeRepository):
        self.equipment_repository = equipment_repository
        self.manufacturer_repository = manufacturer_repository
        self.equipment_type_repository = equipment_type_repository

    def db_populate(self):
        for equipment in self.read_equipments():
            self.equipment_repository.add(equipment)

    def read_equipments(self):
        return read_elements(equipments_csv(), self.build_equipment_type)

    def build_equipment_type(self, row):
        manufacturer = self.manufacturer_repository.get_by_name(row[0])
        equipment_type = self.equipment_type_repository.get_by_name(row[1])
        return Equipment(equipment_id=None, manufacturer_id=manufacturer.id,
                         manufacturer_name=manufacturer.name, type_id=equipment_type.id,
                         type_name=equipment_type.name, name=row[2], description=row[3])
