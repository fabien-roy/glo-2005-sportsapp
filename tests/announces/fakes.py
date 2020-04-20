from instance.announces.fakes import shop1_equipment1_announce1, shop1_equipment2_announce1, \
    shop2_equipment2_announce1, shop2_equipment2_announce2, shop3_equipment1_announce1, \
    shop3_equipment3_announce1
from tests.equipments.fakes import equipment1, equipment2, equipment3, get_equipment
from tests.shops.fakes import shop1, shop2, shop3, get_shop

shop1_equipment1_announce1.id = 1
shop1_equipment1_announce1.shop_id = shop1.id
shop1_equipment1_announce1.equipment_id = equipment1.id

shop1_equipment2_announce1.id = 2
shop1_equipment2_announce1.shop_id = shop1.id
shop1_equipment2_announce1.equipment_id = equipment2.id

shop2_equipment2_announce1.id = 3
shop2_equipment2_announce1.shop_id = shop2.id
shop2_equipment2_announce1.equipment_id = equipment2.id

shop2_equipment2_announce2.id = 4
shop2_equipment2_announce2.shop_id = shop2.id
shop2_equipment2_announce2.equipment_id = equipment2.id

shop3_equipment1_announce1.id = 5
shop3_equipment1_announce1.shop_id = shop3.id
shop3_equipment1_announce1.equipment_id = equipment1.id

shop3_equipment3_announce1.id = 6
shop3_equipment3_announce1.shop_id = shop3.id
shop3_equipment3_announce1.equipment_id = equipment3.id

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
