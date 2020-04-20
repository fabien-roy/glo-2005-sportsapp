from app.equipments.exceptions import EquipmentNotFoundException
from instance.equipments.fakes import equipment1, equipment2, equipment3

equipment1.id = 1
equipment2.id = 2
equipment3.id = 3


def get_equipment(equipment_id):
    int_id = int(equipment_id)
    if int_id == equipment1.id:
        return equipment1
    if int_id == equipment2.id:
        return equipment2
    if int_id == equipment3.id:
        return equipment3

    return None


def no_equipment():
    raise EquipmentNotFoundException


def get_equipments_filtered(form):
    if form is None:
        return [equipment1, equipment2, equipment3]

    return [equipment1]
