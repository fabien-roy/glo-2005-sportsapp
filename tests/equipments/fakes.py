from app.equipments.exceptions import EquipmentNotFoundException
from app.equipments.models import Equipment

equipment1 = Equipment(1, category='hiking', name="Men Wayfinder Mid OutDry Boot",
                       description="Our signature waterproof construction keeps "
                                   "this multisport shoe comfortably dry for "
                                   "any activity—in any weather.")
equipment2 = Equipment(2, category='running', name="Men F.K.T. Lite Trail Running Shoe",
                       description="This lightweight trail runner lets you reach your "
                                   "fastest time without sacrificing performance.")
equipment3 = Equipment(3, category='recovery', name="Men Molokai III Recovery Sandal",
                       description="After a tough trail run there’s nothing more soothing for "
                                   "your feet than the men’s Molokai III Recovery "
                                   "Sandal. Crafted with a supportive midsole"
                                   " and a moldable footbed to fit even the"
                                   " most tortured feet.")


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


def get_announces_for_equipment(equipment_id):
    return get_equipment(equipment_id).announces
