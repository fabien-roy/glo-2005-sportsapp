from app.sports.exceptions import SportNotFoundException
from app.sports.models import Sport

from tests.climates.fakes import climate1, climate2, climate3

sport1 = Sport(sport_id=1, name='Randonnee', climates=[climate1, climate2])
sport2 = Sport(sport_id=2, name='Escalade', climates=[climate2, climate3])
sport3 = Sport(sport_id=3, name='Natation', climates=[climate3])

sport1_no_climates = Sport(sport_id=1, name='Randonnee', climates=[])
sport2_no_climates = Sport(sport_id=2, name='Escalade', climates=[])
sport3_no_climates = Sport(sport_id=3, name='Natation', climates=[])


def get_sport(sport_id):
    int_id = int(sport_id)
    if int_id == sport1.id:
        return sport1
    if int_id == sport2.id:
        return sport2
    if int_id == sport3.id:
        return sport3


def no_sport():
    raise SportNotFoundException


def get_sports_filtered(form):
    if form is None:
        return [sport1, sport2, sport3]
    else:
        return [sport1]


def get_climates_for_sport(sport_id):
    return get_sport(sport_id).climates
