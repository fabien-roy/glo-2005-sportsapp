from app.announces.models import Announce
from instance.equipments.fakes import equipment1, equipment2, equipment3
from instance.shops.fakes import shop1, shop3, shop2

shop1_equipment1_announce1 = Announce(None, shop1.id, shop1.name, equipment1.id, equipment1.name,
                                      'New', 199.99)
shop1_equipment2_announce1 = Announce(None, shop1.id, shop1.name, equipment2.id, equipment2.name,
                                      'Used', 149.99)
shop2_equipment2_announce1 = Announce(None, shop2.id, shop2.name, equipment2.id, equipment2.name,
                                      'New', 400.00)
shop2_equipment2_announce2 = Announce(None, shop2.id, shop2.name, equipment2.id, equipment2.name,
                                      'Needs repair',
                                      300.00)
shop3_equipment1_announce1 = Announce(None, shop3.id, shop3.name, equipment1.id, equipment1.name,
                                      'Used', 49.99)
shop3_equipment3_announce1 = Announce(None, shop3.id, shop3.name, equipment3.id, equipment3.name,
                                      'Used', 99.99)
