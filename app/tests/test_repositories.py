import unittest

from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.repositories.mysql_sport_repositories import MySQLSportRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCenterRepository
from app.sports.exceptions import SportNotFoundException
from app.tests import test_basic
from app.tests.fakes import sport1, sport2, sport3, center1, center3, center2
from instance.db_create import db_create

sport_repository = MySQLSportRepository()
practice_center_repository = MySQLPracticeCenterRepository()


def reset_repositories():
    db_create()


def add_sports():
    reset_repositories()
    sport_repository.add(sport1)
    sport_repository.add(sport2)
    sport_repository.add(sport3)


def add_practice_centers():
    reset_repositories()
    practice_center_repository.add(center1)
    practice_center_repository.add(center2)
    practice_center_repository.add(center3)


class SportRepositoryTests(test_basic.BasicTests):

    def test_get_with_no_sport_should_raise_sport_not_found_exception(self):
        reset_repositories()
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
        reset_repositories()
        sports = sport_repository.get_all()
        self.assertEquals(0, len(sports))

    def test_get_all_get_sports(self):
        add_sports()
        sports = sport_repository.get_all()
        self.assertIn(sport1, sports)
        self.assertIn(sport2, sports)
        self.assertIn(sport3, sports)


class PracticeCenterRepositoryTests(test_basic.BasicTests):

    def test_get_with_no_practice_center_should_raise_practice_center_not_found_exception(self):
        reset_repositories()
        self.assertRaises(PracticeCenterNotFoundException, practice_center_repository.get, 1)

    def test_get_with_non_existent_practice_center_should_raise_practice_center_not_found_exception(self):
        add_practice_centers()
        self.assertRaises(PracticeCenterNotFoundException, practice_center_repository.get, -1)

    def test_get_should_get_practice_center(self):
        add_practice_centers()
        practice_center = practice_center_repository.get(center1.id)
        self.assertEquals(center1, practice_center)
        practice_center = practice_center_repository.get(center2.id)
        self.assertEquals(center2, practice_center)
        practice_center = practice_center_repository.get(center3.id)
        self.assertEquals(center3, practice_center)

    def test_get_all_with_no_practice_center_get_no_practice_center(self):
        reset_repositories()
        practice_centers = practice_center_repository.get_all()
        self.assertEquals(0, len(practice_centers))

    def test_get_all_get_practice_centers(self):
        add_practice_centers()
        practice_centers = practice_center_repository.get_all()
        self.assertIn(center1, practice_centers)
        self.assertIn(center2, practice_centers)
        self.assertIn(center3, practice_centers)


if __name__ == "__main__":
    unittest.main()
