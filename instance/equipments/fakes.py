from app.equipments.models import Equipment
from instance.manufacturers.fakes import manufacturer2, manufacturer1, manufacturer3

equipment1 = Equipment(None, manufacturer=manufacturer1.name, category='hiking',
                       name="Men Wayfinder Mid OutDry Boot",
                       description="Our signature waterproof construction keeps "
                                   "this multisport shoe comfortably dry for "
                                   "any activity—in any weather.")
equipment2 = Equipment(None, manufacturer=manufacturer2.name, category='running',
                       name="Men F.K.T. Lite Trail Running Shoe",
                       description="This lightweight trail runner lets you reach your "
                                   "fastest time without sacrificing performance.")
equipment3 = Equipment(None, manufacturer=manufacturer3.name, category='recovery',
                       name="Men Molokai III Recovery Sandal",
                       description="After a tough trail run there’s nothing more soothing for "
                                   "your feet than the men’s Molokai III Recovery "
                                   "Sandal. Crafted with a supportive midsole"
                                   " and a moldable footbed to fit even the"
                                   " most tortured feet.")
