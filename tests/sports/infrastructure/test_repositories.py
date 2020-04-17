from app.sports.exceptions import SportNotFoundException
from app.sports.infrastructure.repositories import MySQLSportRepository
from tests.climates.mocks import climate_repository
from tests.recommendations.mocks import recommendation_repository
from tests.repositories.mysql_test_database import test_database
from tests.sports.fakes import sport1, sport2, sport3
from tests.sports.forms import FakeSportSearchForm
from tests.test_basic_repositories import BasicRepositoryTests


class SportsRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLSportRepository(test_database, climate_repository,
                                               recommendation_repository)

    def test_get_with_no_sport_should_raise_sport_not_found_exception(self):
        self.recreate_database()
        self.assertRaises(SportNotFoundException, self.repository.get, 1)

    def test_get_with_non_existent_sport_should_raise_sport_not_found_exception(self):
        self.assertRaises(SportNotFoundException, self.repository.get, -1)

    def test_get_should_get_sport(self):
        sport = self.repository.get(sport1.id)
        self.assertEqual(sport1, sport)
        sport = self.repository.get(sport2.id)
        self.assertEqual(sport2, sport)
        sport = self.repository.get(sport3.id)
        self.assertEqual(sport3, sport)

    def test_get_should_get_sport_climates(self):
        sport = self.repository.get(sport1.id)
        self.assertCountEqual(sport1.climates, sport.climates)
        sport = self.repository.get(sport2.id)
        self.assertCountEqual(sport2.climates, sport.climates)
        sport = self.repository.get(sport3.id)
        self.assertCountEqual(sport3.climates, sport.climates)

    def test_get_should_get_sport_recommendations(self):
        sport = self.repository.get(sport1.id)
        self.assertCountEqual(sport1.recommendations, sport.recommendations)
        sport = self.repository.get(sport2.id)
        self.assertCountEqual(sport2.recommendations, sport.recommendations)
        sport = self.repository.get(sport3.id)
        self.assertCountEqual(sport3.recommendations, sport.recommendations)

    def test_get_all_with_no_sport_get_no_sport(self):
        self.recreate_database()
        sports = self.repository.get_all()
        self.assertEqual(0, len(sports))

    def test_get_all_get_sports(self):
        sports = self.repository.get_all()
        self.assertIn(sport1, sports)
        self.assertIn(sport2, sports)
        self.assertIn(sport3, sports)

    def test_get_all_with_all_filter_sports(self):
        form = FakeSportSearchForm(any_field=sport1.name)
        sports = self.repository.get_all(form)
        self.assertIn(sport1, sports)
        self.assertNotIn(sport2, sports)
        self.assertNotIn(sport3, sports)

    def test_get_all_with_name_filter_sports(self):
        form = FakeSportSearchForm(name=sport1.name)
        sports = self.repository.get_all(form)
        self.assertIn(sport1, sports)
        self.assertNotIn(sport2, sports)
        self.assertNotIn(sport3, sports)
