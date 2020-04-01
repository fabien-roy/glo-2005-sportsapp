from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.tests.fakes import sport1, sport2, sport3
from app.tests.test_basic_repositories import BasicRepositoryTests


class ClimatesRepositoryTests(BasicRepositoryTests):

    def setUp(self):
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
        self.add_sports()
        climates = self.repository.get_all_for_sport(sport1.id)
        self.assertCountEqual(sport1.climates, climates)
        climates = self.repository.get_all_for_sport(sport2.id)
        self.assertCountEqual(sport2.climates, climates)
        climates = self.repository.get_all_for_sport(sport3.id)
        self.assertCountEqual(sport3.climates, climates)
