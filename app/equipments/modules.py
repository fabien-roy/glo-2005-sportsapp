from injector import Module

from app.equipments.infrastructure.repositories import MySQLEquipmentRepository
from app.equipments.repositories import EquipmentRepository


class EquipmentModule(Module):
    def configure(self, binder):
        binder.bind(EquipmentRepository, to=MySQLEquipmentRepository)
