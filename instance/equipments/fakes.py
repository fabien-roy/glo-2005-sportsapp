from app.equipments.models import Equipment
from instance.equipment_types.fakes import type1, type3, type2
from instance.manufacturers.fakes import manufacturer2, manufacturer1, manufacturer3

equipment1 = Equipment(None, manufacturer_id=manufacturer1.id, manufacturer_name=manufacturer1.name,
                       type_id=type1.id, type_name=type1.name,
                       name="Men Wayfinder Mid OutDry Boot",
                       description="Our signature waterproof construction keeps "
                                   "this multisport shoe comfortably dry for "
                                   "any activity—in any weather.")
equipment2 = Equipment(None, manufacturer_id=manufacturer2.id, manufacturer_name=manufacturer2.name,
                       type_id=type2.id, type_name=type2.name,
                       name="Men F.K.T. Lite Trail Running Shoe",
                       description="This lightweight trail runner lets you reach your "
                                   "fastest time without sacrificing performance.")
equipment3 = Equipment(None, manufacturer_id=manufacturer3.id, manufacturer_name=manufacturer3.name,
                       type_id=type3.id, type_name=type3.name,
                       name="Men Molokai III Recovery Sandal",
                       description="After a tough trail run there’s nothing more soothing for "
                                   "your feet than the men’s Molokai III Recovery "
                                   "Sandal. Crafted with a supportive midsole"
                                   " and a moldable footbed to fit even the"
                                   " most tortured feet.")
equipmentN = Equipment(None, manufacturer_id=manufacturer3.id, manufacturer_name=manufacturer3.name,
                       type_id=type3.id, type_name=type3.name,
                       name="Test equipment")
