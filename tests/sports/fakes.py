from app.sports.exceptions import SportNotFoundException
from app.sports.models import Sport
from tests.equipment_types.fakes import type1, type2, type3
from instance.sports.fakes import sport1, sport2, sport3

sport1.id = 1
sport2.id = 2
sport3.id = 3

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

    return None


def no_sport():
    raise SportNotFoundException


def get_sports_filtered(form):
    if form is None:
        return [sport1, sport2, sport3]

    return [sport1]


def get_sports_for_equipment_type(type_id):
    int_id = int(type_id)
    if int_id == type1.id:
        return [sport1, sport3]
    if int_id == type2.id:
        return [sport3]
    if int_id == type3.id:
        return [sport1]

    return None


def get_climates_for_sport(sport_id):
    return get_sport(sport_id).climates


def get_equipment_types_for_sport(sport_id):
    return get_sport(sport_id).required_equipment_types
