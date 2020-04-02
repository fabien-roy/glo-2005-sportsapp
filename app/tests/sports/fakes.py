from app.sports.exceptions import SportNotFoundException
from app.sports.models import Sport

from app.tests.climates.fakes import climate1, climate2, climate3

sport1 = Sport(sport_id=1, name='Randonnee', climates=[climate1, climate2])
sport2 = Sport(sport_id=2, name='Escalade', climates=[climate2, climate3])
sport3 = Sport(sport_id=3, name='Natation', climates=[climate3])

sport1_no_climates = Sport(sport_id=1, name='Randonnee', climates=[])
sport2_no_climates = Sport(sport_id=2, name='Escalade', climates=[])
sport3_no_climates = Sport(sport_id=3, name='Natation', climates=[])


def sports(sport_id):
    return {
        '1': sport1,
        '2': sport2,
        '3': sport3
    }[sport_id]


def no_sport():
    raise SportNotFoundException
