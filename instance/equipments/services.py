from app.equipments.repositories import EquipmentRepository
from instance import injector
from instance.equipments.fakes import equipment1, equipment2, equipment3

equipment_repository = injector.get(EquipmentRepository)


def db_populate_with_equipments():
    equipment_repository.add(equipment1)
    equipment_repository.add(equipment2)
    equipment_repository.add(equipment3)
