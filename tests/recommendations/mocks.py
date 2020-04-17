from unittest import mock

from tests.recommendations.fakes import get_recommendations_for_practice_center, \
    get_recommendations_for_sport, get_recommendations_for_sport_and_user, \
    get_recommendations_for_practice_center_and_user

recommendation_repository = mock.Mock()

recommendation_repository.get_all_for_sport.side_effect = get_recommendations_for_sport

recommendation_repository.get_all_for_practice_center.side_effect = \
    get_recommendations_for_practice_center

recommendation_repository.get_all_for_sport_and_user.side_effect = \
    get_recommendations_for_sport_and_user

recommendation_repository.get_all_for_practice_center_and_user.side_effect = \
    get_recommendations_for_practice_center_and_user
