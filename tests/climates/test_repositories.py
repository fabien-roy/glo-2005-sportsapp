import unittest

from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from tests.practice_centers.fakes import center1, center2, center3
from tests.sports.fakes import sport1, sport2, sport3
from tests.test_basic_repositories import BasicRepositoryTests


class ClimatesRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLClimatesRepository()

    def test_get_all_for_sport_should_without_sport_get_no_climate(self):
        self.reset_repositories()
        climates = self.repository.get_all_for_sport(sport1.id)
        self.assertEqual(0, len(climates))
        climates = self.repository.get_all_for_sport(sport2.id)
        self.assertEqual(0, len(climates))
        climates = self.repository.get_all_for_sport(sport3.id)
        self.assertEqual(0, len(climates))

    def test_get_all_for_sport_should_get_sport_climates(self):
        climates = self.repository.get_all_for_sport(sport1.id)
        self.assertCountEqual(sport1.climates, climates)
        climates = self.repository.get_all_for_sport(sport2.id)
        self.assertCountEqual(sport2.climates, climates)
        climates = self.repository.get_all_for_sport(sport3.id)
        self.assertCountEqual(sport3.climates, climates)

    def test_get_all_for_practice_center_should_without_practice_center_get_no_climate(self):
        self.reset_repositories()
        climates = self.repository.get_all_for_practice_center(center1.id)
        self.assertEqual(0, len(climates))
        climates = self.repository.get_all_for_practice_center(center2.id)
        self.assertEqual(0, len(climates))
        climates = self.repository.get_all_for_practice_center(center3.id)
        self.assertEqual(0, len(climates))

    def test_get_all_for_practice_center_should_get_practice_center_climates(self):
        climates = self.repository.get_all_for_practice_center(center1.id)
        self.assertCountEqual(center1.climates, climates)
        climates = self.repository.get_all_for_practice_center(center2.id)
        self.assertCountEqual(center2.climates, climates)
        climates = self.repository.get_all_for_practice_center(center3.id)
        self.assertCountEqual(center3.climates, climates)


if __name__ == "__main__":
    unittest.main()
