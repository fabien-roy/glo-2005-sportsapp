from unittest import mock

from app.tests.practice_centers.mocks import get_practice_center
from app.tests.sports.mocks import get_sport

climates_repository = mock.Mock()


def get_climates_for_sport(sport_id):
    return get_sport(sport_id).climates


climates_repository.get_all_for_sport.side_effect = get_climates_for_sport


def get_climates_for_practice_center(practice_center_id):
    return get_practice_center(practice_center_id).climates


climates_repository.get_all_for_practice_center.side_effect = get_climates_for_practice_center
