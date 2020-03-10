from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.models import PracticeCenter
from app.sports.models import Sport
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


center1 = PracticeCenter(1,
                         name='Mont-Orford National Park',
                         email='parc.mont-orford@sepaq.com',
                         web_site='https://www.sepaq.com/pq/mor/',
                         phone_number='819 843-9855')
center2 = PracticeCenter(2,
                         name='Parc des Montagnards',
                         email='info@censhefford.ca',
                         web_site='https://www.cantonsdelest.com/quoi-faire/980/parc-des-montagnards')
center3 = PracticeCenter(3,
                         name='Gault Nature Reserve of McGill University')


def practice_centers(practice_center_id):
    return {
        '1': center1,
        '2': center2,
        '3': center3
    }[practice_center_id]


def no_practice_center():
    raise PracticeCenterNotFoundException
