from app.announces.models import Announce
from tests.equipments.fakes import equipment1, equipment2, equipment3, get_equipment
from tests.shops.fakes import shop1, shop2, shop3

shop1_equipment1_announce1 = Announce(1, shop1.id, equipment1.id, 'New', 199.99, )
shop1_equipment2_announce1 = Announce(2, shop1.id, equipment2.id, 'Used', 149.99, )
shop2_equipment2_announce1 = Announce(3, shop2.id, equipment2.id, 'New', 400.00, )
shop2_equipment2_announce2 = Announce(4, shop2.id, equipment2.id, 'Needs repair', 300.00, )
shop3_equipment1_announce1 = Announce(5, shop3.id, equipment1.id, 'Used', 49.99, )
shop3_equipment3_announce1 = Announce(6, shop3.id, equipment3.id, 'Used', 99.99, )

shop1.add_announce(shop1_equipment1_announce1)
shop1.add_announce(shop1_equipment2_announce1)
shop2.add_announce(shop2_equipment2_announce1)
shop2.add_announce(shop2_equipment2_announce2)
shop3.add_announce(shop3_equipment1_announce1)
shop3.add_announce(shop3_equipment3_announce1)

equipment1.add_announce(shop1_equipment1_announce1)
equipment1.add_announce(shop3_equipment1_announce1)
equipment2.add_announce(shop1_equipment2_announce1)
equipment2.add_announce(shop2_equipment2_announce1)
equipment2.add_announce(shop2_equipment2_announce2)
equipment3.add_announce(shop3_equipment3_announce1)


def get_announces_for_shop(shop_id):
    return get_shop(shop_id).announces


def get_announces_for_equipment(equipment_id):
    return get_equipment(equipment_id).announces
