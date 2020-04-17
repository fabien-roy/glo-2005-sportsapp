from app.sports.models import Sport
from instance.climates.fakes import climate1, climate2, climate3

sport1 = Sport(None, name='Randonnee', climates=[climate1, climate2])
sport2 = Sport(None, name='Escalade', climates=[climate2, climate3])
sport3 = Sport(None, name='Natation', climates=[climate3])
