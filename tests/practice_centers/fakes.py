from app.practice_centers.exceptions import PracticeCenterNotFoundException
from instance.practice_centers.fakes import center1, center2, center3
from tests.climates.fakes import climate1, climate2, climate3

center1.id = 1
center1.climates = [climate2]
center1.average_note = 5.00
center2.id = 2
center2.climates = []
center2.average_note = 2.50
center3.id = 3
center3.climates = [climate1, climate3]
center3.average_note = 2.00


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
