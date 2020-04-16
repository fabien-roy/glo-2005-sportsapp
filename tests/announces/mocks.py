from unittest import mock

from tests.announces.fakes import get_announces_for_shop, get_announces_for_equipment

announces_repository = mock.Mock()


announces_repository.get_all_for_shop.side_effect = get_announces_for_shop


announces_repository.get_all_for_equipment.side_effect = get_announces_for_equipment
