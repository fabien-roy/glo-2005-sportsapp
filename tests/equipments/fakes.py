from app.equipments.exceptions import EquipmentNotFoundException
from instance.equipments.fakes import equipment1, equipment2, equipment3
from instance.sports.fakes import sport3, sport1
from tests.manufacturers.fakes import manufacturer1, manufacturer2, manufacturer3

equipment1.id = 1
equipment1.manufacturer_id = manufacturer1.id
equipment1.associated_sports = [sport1, sport3]
equipment2.id = 2
equipment2.manufacturer_id = manufacturer2.id
equipment2.associated_sports = [sport3]
equipment3.id = 3
equipment3.manufacturer_id = manufacturer3.id
equipment2.associated_sports = [sport1]


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
