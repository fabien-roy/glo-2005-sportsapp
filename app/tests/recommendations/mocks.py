from unittest import mock

from app.tests.practice_centers.mocks import get_practice_center
from app.tests.sports.mocks import get_sport
from app.tests.users.mocks import get_user

recommendations_repository = mock.Mock()


def get_recommendations_for_sport(sport_id):
    return get_sport(sport_id).recommendations


recommendations_repository.get_all_for_sport.side_effect = get_recommendations_for_sport


def get_recommendations_for_practice_center(practice_center_id):
    return get_practice_center(practice_center_id).recommendations


recommendations_repository.get_all_for_practice_center.side_effect = \
    get_recommendations_for_practice_center


def get_recommendations_for_sport_and_user(user_id):
    return get_user(user_id).sport_recommendations


recommendations_repository.get_all_for_sport_and_user.side_effect = get_recommendations_for_sport_and_user


def get_recommendations_for_practice_center_and_user(user_id):
    return get_user(user_id).practice_center_recommendations


recommendations_repository.get_all_for_practice_center_and_user.side_effect = \
    get_recommendations_for_practice_center_and_user
