from unittest import mock

from tests.sports.fakes import get_equipment_types_for_sport

equipment_type_repository = mock.Mock()


equipment_type_repository.get_all_for_sport.side_effect = get_equipment_types_for_sport
