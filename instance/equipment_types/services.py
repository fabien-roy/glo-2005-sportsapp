from injector import inject

from app.equipment_types.repositories import EquipmentTypeRepository
from instance.equipment_types.fakes import type1, type2, type3


class EquipmentTypePopulationService:
    @inject
    def __init__(self, equipment_type_repository: EquipmentTypeRepository):
        self.equipment_type_repository = equipment_type_repository

    def db_populate(self):
        self.equipment_type_repository.add(type1)
        self.equipment_type_repository.add(type2)
        self.equipment_type_repository.add(type3)
