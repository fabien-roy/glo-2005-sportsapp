from app.models import Sport
from app.sports.exceptions import SportNotFoundException

sport1 = Sport(sport_id=1, name='Randonnee')
sport2 = Sport(sport_id=2, name='Escalade')
sport3 = Sport(sport_id=3, name='Natation')


def sports(sport_id):
    return {
        '1': sport1,
        '2': sport2,
        '3': sport3
    }[sport_id]


def no_sport():
    raise SportNotFoundException
