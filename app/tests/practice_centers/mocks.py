from unittest import mock

from app.tests.fakes import center1, center2, center3

practice_centers_repository = mock.Mock()


def get_practice_center(practice_center_id):
    if practice_center_id == center1.id:
        return center1
    if practice_center_id == center2.id:
        return center2
    if practice_center_id == center3.id:
        return center3
