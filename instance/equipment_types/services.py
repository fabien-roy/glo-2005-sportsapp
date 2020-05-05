from injector import inject

from app.equipment_types.models import EquipmentType
from app.equipment_types.repositories import EquipmentTypeRepository
from instance.equipment_types.fakes import type1, type2, type3
from instance.resources.helpers import read_elements, equipment_types_csv


class EquipmentTypePopulationService:
    @inject
    def __init__(self, equipment_type_repository: EquipmentTypeRepository):
        self.equipment_type_repository = equipment_type_repository

    def db_populate(self):
        for equipment_type in self.read_equipment_types():
            self.equipment_type_repository.add(equipment_type)

    def read_equipment_types(self):
        return read_elements(equipment_types_csv(), self.build_equipment_type)

    @staticmethod
    def build_equipment_type(row):
        return EquipmentType(type_id=None, name=row[0])
