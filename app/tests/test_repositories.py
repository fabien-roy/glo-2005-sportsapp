import unittest

from app.repositories.mysql_sport_repositories import MySQLSportRepository as SportRepository
from app.sports.exceptions import SportNotFoundException
from app.tests import test_basic
from app.tests.fakes import sport1, sport2, sport3
from instance.db_create import db_create

sport_repository = SportRepository()


def remove_sports():
    db_create()


def add_sports():
    remove_sports()
    sport_repository.add(sport1)
    sport_repository.add(sport2)
    sport_repository.add(sport3)


class SportRepositoryTests(test_basic.BasicTests):

    def test_get_with_no_sport_should_raise_sport_not_found_exception(self):
        remove_sports()
        self.assertRaises(SportNotFoundException, sport_repository.get, 1)

    def test_get_with_non_existent_sport_should_raise_sport_not_found_exception(self):
        add_sports()
        self.assertRaises(SportNotFoundException, sport_repository.get, -1)

    def test_get_should_get_sport(self):
        add_sports()
        sport = sport_repository.get(sport1.id)
        self.assertEquals(sport1, sport)
        sport = sport_repository.get(sport2.id)
        self.assertEquals(sport2, sport)
        sport = sport_repository.get(sport3.id)
        self.assertEquals(sport3, sport)

    def test_get_all_with_no_sport_get_no_sport(self):
        remove_sports()
        sports = sport_repository.get_all()
        self.assertEquals(0, len(sports))

    def test_get_all_get_sports(self):
        add_sports()
        sports = sport_repository.get_all()
        self.assertIn(sport1, sports)
        self.assertIn(sport2, sports)
        self.assertIn(sport3, sports)


if __name__ == "__main__":
    unittest.main()
