from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.sports.exceptions import SportNotFoundException
from app.tests.fakes import sport1, sport2, sport3
from app.tests.forms import FakeSportsForm
from app.tests.test_basic_repositories import BasicRepositoryTests


class SportsRepositoryTests(BasicRepositoryTests):

    sport_repository = MySQLSportsRepository()

    def test_get_with_no_sport_should_raise_sport_not_found_exception(self):
        self.reset_repositories()
        self.assertRaises(SportNotFoundException, self.sport_repository.get, 1)

    def test_get_with_non_existent_sport_should_raise_sport_not_found_exception(self):
        self.add_sports()
        self.assertRaises(SportNotFoundException, self.sport_repository.get, -1)

    def test_get_should_get_sport(self):
        self.add_sports()
        sport = self.sport_repository.get(sport1.id)
        self.assertEqual(sport1, sport)
        sport = self.sport_repository.get(sport2.id)
        self.assertEqual(sport2, sport)
        sport = self.sport_repository.get(sport3.id)
        self.assertEqual(sport3, sport)

    def test_get_should_get_sport_climates(self):
        self.add_sports()
        sport = self.sport_repository.get(sport1.id)
        self.assertCountEqual(sport1.climates, sport.climates)
        sport = self.sport_repository.get(sport2.id)
        self.assertCountEqual(sport2.climates, sport.climates)
        sport = self.sport_repository.get(sport3.id)
        self.assertCountEqual(sport3.climates, sport.climates)

    def test_get_should_get_sport_recommendations(self):
        self.add_sports_recommendations()
        sport = self.sport_repository.get(sport1.id)
        self.assertCountEqual(sport1.recommendations, sport.recommendations)
        sport = self.sport_repository.get(sport2.id)
        self.assertCountEqual(sport2.recommendations, sport.recommendations)
        sport = self.sport_repository.get(sport3.id)
        self.assertCountEqual(sport3.recommendations, sport.recommendations)

    def test_get_all_with_no_sport_get_no_sport(self):
        self.reset_repositories()
        sports = self.sport_repository.get_all()
        self.assertEqual(0, len(sports))

    def test_get_all_get_sports(self):
        self.add_sports()
        sports = self.sport_repository.get_all()
        self.assertIn(sport1, sports)
        self.assertIn(sport2, sports)
        self.assertIn(sport3, sports)

    def test_get_all_with_name_filter_sports(self):
        self.add_sports()
        form = FakeSportsForm(sport1.name)
        sports = self.sport_repository.get_all(form)
        self.assertIn(sport1, sports)
        self.assertNotIn(sport2, sports)
        self.assertNotIn(sport3, sports)
