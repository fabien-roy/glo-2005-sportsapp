from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.models import PracticeCenter
from tests.climates.fakes import climate2, climate1, climate3

center1 = PracticeCenter(1,
                         name='Mont-Orford National Park',
                         email='parc.mont-orford@sepaq.com',
                         web_site='https://www.sepaq.com/pq/mor/',
                         phone_number='819 843-9855',
                         climates=[climate2])
center2 = PracticeCenter(2,
                         name='Parc des Montagnards',
                         email='info@censhefford.ca',
                         web_site=
                         'https://www.cantonsdelest.com/quoi-faire/980/parc-des-montagnards',
                         climates=[])
center3 = PracticeCenter(3,
                         name='Gault Nature Reserve of McGill University',
                         climates=[climate1, climate3])


def get_practice_center(practice_center_id):
    int_id = int(practice_center_id)
    if int_id == center1.id:
        return center1
    if int_id == center2.id:
        return center2
    if int_id == center3.id:
        return center3

    return None


def no_practice_center():
    raise PracticeCenterNotFoundException


def get_practice_centers_filtered(form):
    if form is None:
        return [center1, center2, center3]

    return [center1]


def get_climates_for_practice_center(practice_center_id):
    return get_practice_center(practice_center_id).climates
