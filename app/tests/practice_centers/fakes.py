from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.models import PracticeCenter

from app.tests.climates.fakes import climate1, climate3, climate2

center1 = PracticeCenter(1,
                         name='Mont-Orford National Park',
                         email='parc.mont-orford@sepaq.com',
                         web_site='https://www.sepaq.com/pq/mor/',
                         phone_number='819 843-9855',
                         climates=[climate2])
center2 = PracticeCenter(2,
                         name='Parc des Montagnards',
                         email='info@censhefford.ca',
                         web_site='https://www.cantonsdelest.com/quoi-faire/980/parc-des-montagnards',
                         climates=[])
center3 = PracticeCenter(3,
                         name='Gault Nature Reserve of McGill University',
                         climates=[climate1, climate3])


def practice_centers(practice_center_id):
    return {
        '1': center1,
        '2': center2,
        '3': center3
    }[practice_center_id]


def no_practice_center():
    raise PracticeCenterNotFoundException
