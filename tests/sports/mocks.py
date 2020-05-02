from unittest import mock

from tests.sports.fakes import get_sports_for_equipment_type

sport_repository = mock.Mock()

sport_repository.get_all_for_equipment_type.side_effect = get_sports_for_equipment_type
