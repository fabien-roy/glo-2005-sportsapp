import unittest

from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.repositories.mysql_climate_repositories import MySQLClimateRepository
from app.repositories.mysql_sport_repositories import MySQLSportRepository, MySQLSportClimateRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCenterRepository
from app.repositories.mysql_user_repositories import MySQLUserRepository
from app.sports.exceptions import SportNotFoundException
from app.tests import test_basic
from app.tests.fakes import sport1, sport2, sport3, center1, center3, center2, climate1, climate2, climate3, user2, \
    user1, user3, sport1_recommendation1, sport2_recommendation1, sport2_recommendation2, sport3_recommendation1, \
    center1_recommendation1, center2_recommendation1, center2_recommendation2, center3_recommendation1, \
    center3_recommendation2
from app.users.exceptions import UserNotFoundException
from instance.db_create import db_create

sport_repository = MySQLSportRepository()
practice_center_repository = MySQLPracticeCenterRepository()
climate_repository = MySQLClimateRepository()
sport_climate_repository = MySQLSportClimateRepository()
user_repository = MySQLUserRepository()


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


def add_practice_centers():
    reset_repositories()
    add_climates()
    practice_center_repository.add(center1)
    practice_center_repository.add(center2)
    practice_center_repository.add(center3)


def add_practice_centers_recommendations():
    reset_repositories()
    add_practice_centers()
    add_users()
    practice_center_repository.add_recommendation(center1.id, center1_recommendation1)
    practice_center_repository.add_recommendation(center2.id, center2_recommendation1)
    practice_center_repository.add_recommendation(center2.id, center2_recommendation2)
    practice_center_repository.add_recommendation(center3.id, center3_recommendation1)
    practice_center_repository.add_recommendation(center3.id, center3_recommendation2)


def add_climates():
    climate_repository.add(climate1)
    climate_repository.add(climate2)
    climate_repository.add(climate3)


def add_users():
    user_repository.add(user1)
    user_repository.add(user2)
    user_repository.add(user3)


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
        self.assertEqual(center1, practice_center)
        practice_center = practice_center_repository.get(center2.id)
        self.assertEqual(center2, practice_center)
        practice_center = practice_center_repository.get(center3.id)
        self.assertEqual(center3, practice_center)

    def test_get_should_get_practice_center_climates(self):
        add_practice_centers()
        practice_center = practice_center_repository.get(center1.id)
        self.assertCountEqual(center1.climates, practice_center.climates)
        practice_center = practice_center_repository.get(center2.id)
        self.assertCountEqual(center2.climates, practice_center.climates)
        practice_center = practice_center_repository.get(center3.id)
        self.assertCountEqual(center3.climates, practice_center.climates)

    def test_get_should_get_practice_center_recommendations(self):
        add_practice_centers_recommendations()
        practice_center = practice_center_repository.get(center1.id)
        self.assertCountEqual(center1.recommendations, practice_center.recommendations)
        practice_center = practice_center_repository.get(center2.id)
        self.assertCountEqual(center2.recommendations, practice_center.recommendations)
        practice_center = practice_center_repository.get(center3.id)
        self.assertCountEqual(center3.recommendations, practice_center.recommendations)

    def test_get_all_with_no_practice_center_get_no_practice_center(self):
        reset_repositories()
        practice_centers = practice_center_repository.get_all()
        self.assertEqual(0, len(practice_centers))

    def test_get_all_get_practice_centers(self):
        add_practice_centers()
        practice_centers = practice_center_repository.get_all()
        self.assertIn(center1, practice_centers)
        self.assertIn(center2, practice_centers)
        self.assertIn(center3, practice_centers)


class UserRepositoryTests(test_basic.BasicTests):

    def test_get_with_no_user_should_raise_user_not_found_exception(self):
        reset_repositories()
        self.assertRaises(UserNotFoundException, user_repository.get, 1)

    def test_get_with_non_existent_user_should_raise_user_not_found_exception(self):
        add_users()
        self.assertRaises(UserNotFoundException, user_repository.get, -1)

    def test_get_should_get_user(self):
        add_users()
        user = user_repository.get(user1.username)
        self.assertEqual(user1, user)
        user = user_repository.get(user2.username)
        self.assertEqual(user2, user)
        user = user_repository.get(user3.username)
        self.assertEqual(user3, user)

    def test_get_all_with_no_practice_center_get_no_practice_center(self):
        reset_repositories()
        users = user_repository.get_all()
        self.assertEqual(0, len(users))

    def test_get_all_get_practice_centers(self):
        add_users()
        users = user_repository.get_all()
        self.assertIn(user1, users)
        self.assertIn(user2, users)
        self.assertIn(user3, users)


if __name__ == "__main__":
    unittest.main()
