from unittest import mock

from tests.practice_centers.fakes import get_climates_for_practice_center
from tests.sports.fakes import get_climates_for_sport

climates_repository = mock.Mock()


climates_repository.get_all_for_sport.side_effect = get_climates_for_sport


climates_repository.get_all_for_practice_center.side_effect = get_climates_for_practice_center
