from unittest import mock

from app.tests.sports.fakes import sport1, sport2, sport3

sports_repository = mock.Mock()


def get_sport(sport_id):
    if sport_id == sport1.id:
        return sport1
    if sport_id == sport2.id:
        return sport2
    if sport_id == sport3.id:
        return sport3
