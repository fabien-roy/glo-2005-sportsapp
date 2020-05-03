from injector import Module

from app.equipment_types.repositories import EquipmentTypeRepository
from tests.equipment_types.mocks import equipment_type_repository


class MockEquipmentTypeModule(Module):
    def configure(self, binder):
        binder.bind(EquipmentTypeRepository, to=equipment_type_repository)
