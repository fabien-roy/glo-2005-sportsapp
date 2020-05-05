from app.announces.models import Announce
from tests.equipments.fakes import equipment1, equipment2, equipment3, get_equipment
from tests.shops.fakes import shop1, shop2, shop3, get_shop

shop1_equipment1_announce1 = Announce(1, shop1.id, shop1.name, equipment1.id, equipment1.name,
                                      'New', 199.99)
shop1_equipment2_announce1 = Announce(2, shop1.id, shop1.name, equipment2.id, equipment2.name,
                                      'Used', 149.99)
shop2_equipment2_announce1 = Announce(3, shop2.id, shop2.name, equipment2.id, equipment2.name,
                                      'New', 400.00)
shop2_equipment2_announce2 = Announce(4, shop2.id, shop2.name, equipment2.id, equipment2.name,
                                      'Needs repair',
                                      300.00)
shop3_equipment1_announce1 = Announce(5, shop3.id, shop3.name, equipment1.id, equipment1.name,
                                      'Used', 49.99)
shop3_equipment3_announce1 = Announce(6, shop3.id, shop3.name, equipment3.id, equipment3.name,
                                      'Used', 99.99)

shop1.announces = [shop1_equipment1_announce1, shop1_equipment2_announce1]
shop2.announces = [shop2_equipment2_announce1, shop2_equipment2_announce2]
shop3.announces = [shop3_equipment1_announce1, shop3_equipment3_announce1]

equipment1.announces = [shop1_equipment1_announce1, shop3_equipment1_announce1]
equipment2.announces = [shop1_equipment2_announce1, shop2_equipment2_announce1,
                        shop2_equipment2_announce2]
equipment3.announces = [shop3_equipment3_announce1]


def get_announces_for_shop(shop_id):
    return get_shop(shop_id).announces


def get_announces_for_equipment(equipment_id):
    return get_equipment(equipment_id).announces
