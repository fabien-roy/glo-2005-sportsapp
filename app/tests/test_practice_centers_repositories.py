from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.tests import test_basic
from app.tests.fakes import center1, center3, center2, climate1, climate2, climate3, user2, \
    user1, user3, center1_recommendation1_user1, center2_recommendation1_user1, center2_recommendation2_user2, center3_recommendation1_user3, \
    center3_recommendation2_user1
from app.tests.forms import FakePracticeCentersForm
from instance.db_create import db_create

sport_repository = MySQLSportsRepository()
practice_center_repository = MySQLPracticeCentersRepository()
climate_repository = MySQLClimatesRepository()
recommendation_repository = MySQLRecommendationsRepository()
user_repository = MySQLUsersRepository()


def reset_repositories():
    db_create()


def add_climates():
    climate_repository.add(climate1)
    climate_repository.add(climate2)
    climate_repository.add(climate3)


def add_users():
    user_repository.add(user1)
    user_repository.add(user2)
    user_repository.add(user3)


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
    recommendation_repository.add_for_practice_center(center1_recommendation1_user1, center1)
    recommendation_repository.add_for_practice_center(center2_recommendation1_user1, center2)
    recommendation_repository.add_for_practice_center(center2_recommendation2_user2, center2)
    recommendation_repository.add_for_practice_center(center3_recommendation1_user3, center3)
    recommendation_repository.add_for_practice_center(center3_recommendation2_user1, center3)


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

    def test_get_all_with_all_filter_practice_centers(self):
        add_practice_centers()
        form = FakePracticeCentersForm(all=center1.name)
        practice_centers = practice_center_repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_name_filter_practice_centers(self):
        add_practice_centers()
        form = FakePracticeCentersForm(name=center1.name)
        practice_centers = practice_center_repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_email_filter_practice_centers(self):
        add_practice_centers()
        form = FakePracticeCentersForm(email=center1.email)
        practice_centers = practice_center_repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_web_site_filter_practice_centers(self):
        add_practice_centers()
        form = FakePracticeCentersForm(web_site=center1.web_site)
        practice_centers = practice_center_repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_phone_number_filter_practice_centers(self):
        add_practice_centers()
        form = FakePracticeCentersForm(phone_number=center1.phone_number)
        practice_centers = practice_center_repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)
