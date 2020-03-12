from app.repositories.mysql_climate_repositories import MySQLClimateRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.repositories.mysql_sport_repositories import MySQLSportsRepository, MySQLSportClimateRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.sports.exceptions import SportNotFoundException
from app.tests import test_basic
from app.tests.fakes import sport1, sport2, sport3, climate1, climate2, climate3, user2, \
    user1, user3, sport1_recommendation1, sport2_recommendation1, sport2_recommendation2, sport3_recommendation1
from instance.db_create import db_create

sport_repository = MySQLSportsRepository()
practice_center_repository = MySQLPracticeCentersRepository()
climate_repository = MySQLClimateRepository()
sport_climate_repository = MySQLSportClimateRepository()
user_repository = MySQLUsersRepository()


def reset_repositories():
    db_create()


def add_sports():
    reset_repositories()
    add_climates()
    sport_repository.add(sport1)
    sport_repository.add(sport2)
    sport_repository.add(sport3)


def add_sports_recommendations():
    reset_repositories()
    add_sports()
    add_users()
    sport_repository.add_recommendation(sport1.id, sport1_recommendation1)
    sport_repository.add_recommendation(sport2.id, sport2_recommendation1)
    sport_repository.add_recommendation(sport2.id, sport2_recommendation2)
    sport_repository.add_recommendation(sport3.id, sport3_recommendation1)


def add_climates():
    climate_repository.add(climate1)
    climate_repository.add(climate2)
    climate_repository.add(climate3)


def add_users():
    user_repository.add(user1)
    user_repository.add(user2)
    user_repository.add(user3)


class SportsRepositoryTests(test_basic.BasicTests):

    def test_get_with_no_sport_should_raise_sport_not_found_exception(self):
        reset_repositories()
        self.assertRaises(SportNotFoundException, sport_repository.get, 1)

    def test_get_with_non_existent_sport_should_raise_sport_not_found_exception(self):
        add_sports()
        self.assertRaises(SportNotFoundException, sport_repository.get, -1)

    def test_get_should_get_sport(self):
        add_sports()
        sport = sport_repository.get(sport1.id)
        self.assertEqual(sport1, sport)
        sport = sport_repository.get(sport2.id)
        self.assertEqual(sport2, sport)
        sport = sport_repository.get(sport3.id)
        self.assertEqual(sport3, sport)

    def test_get_should_get_sport_climates(self):
        add_sports()
        sport = sport_repository.get(sport1.id)
        self.assertCountEqual(sport1.climates, sport.climates)
        sport = sport_repository.get(sport2.id)
        self.assertCountEqual(sport2.climates, sport.climates)
        sport = sport_repository.get(sport3.id)
        self.assertCountEqual(sport3.climates, sport.climates)

    def test_get_should_get_sport_recommendations(self):
        add_sports_recommendations()
        sport = sport_repository.get(sport1.id)
        self.assertCountEqual(sport1.recommendations, sport.recommendations)
        sport = sport_repository.get(sport2.id)
        self.assertCountEqual(sport2.recommendations, sport.recommendations)
        sport = sport_repository.get(sport3.id)
        self.assertCountEqual(sport3.recommendations, sport.recommendations)

    def test_get_all_with_no_sport_get_no_sport(self):
        reset_repositories()
        sports = sport_repository.get_all()
        self.assertEqual(0, len(sports))

    def test_get_all_get_sports(self):
        add_sports()
        sports = sport_repository.get_all()
        self.assertIn(sport1, sports)
        self.assertIn(sport2, sports)
        self.assertIn(sport3, sports)
