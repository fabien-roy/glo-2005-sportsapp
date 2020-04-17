from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.infrastructure.repositories import MySQLPracticeCenterRepository
from tests.climates.mocks import climates_repository
from tests.practice_centers.fakes import center1, center2, center3
from tests.practice_centers.forms import FakePracticeCenterSearchForm
from tests.recommendations.mocks import recommendations_repository
from tests.repositories.mysql_test_database import test_database
from tests.test_basic_repositories import BasicRepositoryTests


class PracticeCenterRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLPracticeCenterRepository(test_database, climates_repository,
                                                        recommendations_repository)

    def test_get_with_no_practice_center_should_raise_practice_center_not_found_exception(self):
        self.recreate_database()
        self.assertRaises(PracticeCenterNotFoundException, self.repository.get, 1)

    def test_get_with_non_existent_center_should_raise_practice_center_not_found_exception(self):
        self.assertRaises(PracticeCenterNotFoundException, self.repository.get, -1)

    def test_get_should_get_practice_center(self):
        practice_center = self.repository.get(center1.id)
        self.assertEqual(center1, practice_center)
        practice_center = self.repository.get(center2.id)
        self.assertEqual(center2, practice_center)
        practice_center = self.repository.get(center3.id)
        self.assertEqual(center3, practice_center)

    def test_get_should_get_practice_center_climates(self):
        practice_center = self.repository.get(center1.id)
        self.assertCountEqual(center1.climates, practice_center.climates)
        practice_center = self.repository.get(center2.id)
        self.assertCountEqual(center2.climates, practice_center.climates)
        practice_center = self.repository.get(center3.id)
        self.assertCountEqual(center3.climates, practice_center.climates)

    def test_get_should_get_practice_center_recommendations(self):
        practice_center = self.repository.get(center1.id)
        self.assertCountEqual(center1.recommendations, practice_center.recommendations)
        practice_center = self.repository.get(center2.id)
        self.assertCountEqual(center2.recommendations, practice_center.recommendations)
        practice_center = self.repository.get(center3.id)
        self.assertCountEqual(center3.recommendations, practice_center.recommendations)

    def test_get_all_with_no_practice_center_get_no_practice_center(self):
        self.recreate_database()
        practice_centers = self.repository.get_all()
        self.assertEqual(0, len(practice_centers))

    def test_get_all_get_practice_centers(self):
        practice_centers = self.repository.get_all()
        self.assertIn(center1, practice_centers)
        self.assertIn(center2, practice_centers)
        self.assertIn(center3, practice_centers)

    def test_get_all_with_all_filter_practice_centers(self):
        form = FakePracticeCenterSearchForm(any_field=center1.name)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_name_filter_practice_centers(self):
        form = FakePracticeCenterSearchForm(name=center1.name)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_email_filter_practice_centers(self):
        form = FakePracticeCenterSearchForm(email=center1.email)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_web_site_filter_practice_centers(self):
        form = FakePracticeCenterSearchForm(web_site=center1.web_site)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_phone_number_filter_practice_centers(self):
        form = FakePracticeCenterSearchForm(phone_number=center1.phone_number)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)
