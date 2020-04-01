from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.tests.fakes import center1, center3, center2
from app.tests.forms import FakePracticeCentersForm
from app.tests.mocks import climates_repository, recommendations_repository
from app.tests.test_basic_repositories import BasicRepositoryTests


def get_climates_for_practice_center(practice_center_id):
    return get_practice_center(practice_center_id).climates


def get_recommendations_for_practice_center(practice_center_id):
    return get_practice_center(practice_center_id).recommendations


def get_practice_center(practice_center_id):
    if practice_center_id == center1.id:
        return center1
    if practice_center_id == center2.id:
        return center2
    if practice_center_id == center3.id:
        return center3


class PracticeCenterRepositoryTests(BasicRepositoryTests):

    def setUp(self):
        super().setUp()
        climates_repository.get_all_for_practice_center.side_effect = get_climates_for_practice_center
        recommendations_repository.get_all_for_practice_center.side_effect = get_recommendations_for_practice_center
        self.repository = MySQLPracticeCentersRepository(climates_repository, recommendations_repository)

    def test_get_with_no_practice_center_should_raise_practice_center_not_found_exception(self):
        self.reset_repositories()
        self.assertRaises(PracticeCenterNotFoundException, self.repository.get, 1)

    def test_get_with_non_existent_practice_center_should_raise_practice_center_not_found_exception(self):
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
        self.reset_repositories()
        practice_centers = self.repository.get_all()
        self.assertEqual(0, len(practice_centers))

    def test_get_all_get_practice_centers(self):
        practice_centers = self.repository.get_all()
        self.assertIn(center1, practice_centers)
        self.assertIn(center2, practice_centers)
        self.assertIn(center3, practice_centers)

    def test_get_all_with_all_filter_practice_centers(self):
        form = FakePracticeCentersForm(all=center1.name)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_name_filter_practice_centers(self):
        form = FakePracticeCentersForm(name=center1.name)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_email_filter_practice_centers(self):
        form = FakePracticeCentersForm(email=center1.email)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_web_site_filter_practice_centers(self):
        form = FakePracticeCentersForm(web_site=center1.web_site)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)

    def test_get_all_with_phone_number_filter_practice_centers(self):
        form = FakePracticeCentersForm(phone_number=center1.phone_number)
        practice_centers = self.repository.get_all(form)
        self.assertIn(center1, practice_centers)
        self.assertNotIn(center2, practice_centers)
        self.assertNotIn(center3, practice_centers)
