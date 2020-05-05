from app.equipments.exceptions import EquipmentNotFoundException
from app.equipments.models import Equipment
from tests.equipment_types.fakes import type1, type2, type3
from tests.sports.fakes import sport3, sport1
from tests.manufacturers.fakes import manufacturer1, manufacturer2, manufacturer3

equipment1 = Equipment(1, type_id=type1.id, type_name=type1.name,
                       manufacturer_id=manufacturer1.id, manufacturer_name=manufacturer1.name,
                       name="Men Wayfinder Mid OutDry Boot",
                       description="Our signature waterproof construction keeps "
                                   "this multisport shoe comfortably dry for "
                                   "any activity—in any weather.")
equipment2 = Equipment(2, type_id=type2.id, type_name=type2.name,
                       manufacturer_id=manufacturer2.id, manufacturer_name=manufacturer2.name,
                       name="Men F.K.T. Lite Trail Running Shoe",
                       description="This lightweight trail runner lets you reach your "
                                   "fastest time without sacrificing performance.")
equipment3 = Equipment(3, type_id=type3.id, type_name=type3.name,
                       manufacturer_id=manufacturer3.id, manufacturer_name=manufacturer3.name,
                       name="Men Molokai III Recovery Sandal",
                       description="After a tough trail run there’s nothing more soothing for "
                                   "your feet than the men’s Molokai III Recovery "
                                   "Sandal. Crafted with a supportive midsole"
                                   " and a moldable footbed to fit even the"
                                   " most tortured feet.")

equipment1.associated_sports = [sport1, sport3]
equipment2.associated_sports = [sport3]
equipment3.associated_sports = [sport1]


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
