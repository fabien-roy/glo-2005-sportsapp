from injector import Module

from app.equipments.repositories import EquipmentRepository
from tests.equipments.mocks import equipment_repository


class MockEquipmentModule(Module):
    def configure(self, binder):
        binder.bind(EquipmentRepository, to=equipment_repository)
