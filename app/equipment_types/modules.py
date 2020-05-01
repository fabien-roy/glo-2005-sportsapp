from injector import Module

from app.equipment_types.infrastructure.repositories import MySQLEquipmentTypeRepository
from app.equipment_types.repositories import EquipmentTypeRepository


class EquipmentTypeModule(Module):
    def configure(self, binder):
        binder.bind(EquipmentTypeRepository, to=MySQLEquipmentTypeRepository)
