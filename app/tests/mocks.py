from unittest import mock

from app.tests.helpers import get_climates_for_sport, get_climates_for_practice_center, get_recommendations_for_sport, \
    get_recommendations_for_practice_center, get_recommendations_for_sport_and_user, \
    get_recommendations_for_practice_center_and_user

climates_repository = mock.Mock()
recommendations_repository = mock.Mock()
sports_repository = mock.Mock()
practice_centers_repository = mock.Mock()
users_repository = mock.Mock()

climates_repository.get_all_for_sport.side_effect = get_climates_for_sport
climates_repository.get_all_for_practice_center.side_effect = get_climates_for_practice_center
recommendations_repository.get_all_for_sport.side_effect = get_recommendations_for_sport
recommendations_repository.get_all_for_practice_center.side_effect = \
    get_recommendations_for_practice_center
recommendations_repository.get_all_for_sport_and_user.side_effect = get_recommendations_for_sport_and_user
recommendations_repository.get_all_for_practice_center_and_user.side_effect = \
    get_recommendations_for_practice_center_and_user
