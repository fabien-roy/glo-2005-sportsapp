from app.sports.models import Sport
from instance.climates.fakes import climate1, climate2, climate3
from instance.equipment_types.fakes import type3, type1, type2

sport1 = Sport(None, name='Randonnee', climates=[climate1, climate2],
               required_equipment_types=[type1, type3])
sport2 = Sport(None, name='Escalade', climates=[climate2, climate3])
sport3 = Sport(None, name='Natation', climates=[climate3], required_equipment_types=[type1, type2])
