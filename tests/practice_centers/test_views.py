import unittest

from tests.practice_centers.fakes import center1, center2, center3
from tests.test_basic_views import BasicViewTests


class PracticeCentersViewsTests(BasicViewTests):

    def get_path(self):
        return '/practice-centers'

    def get_view_title(self):
        return 'Practice Centers'

    def test_practice_centers_with_no_practice_center_should_display_no_practice_center(self):
        self.remove_practice_centers()
        response = self.request_get()
        self.assert_page_is_found(response)
        self.assert_items_are_not_listed(response, [center1.name, center2.name, center3.name])

    def test_practice_centers_with_practice_centers_should_display_practice_centers(self):
        response = self.request_get()
        self.assert_page_is_found(response)
        self.assert_items_are_listed(response, [center1.name, center2.name, center3.name])

    def test_practice_centers_with_form_should_display_filtered_practice_centers(self):
        response = self.request_post()
        self.assert_page_is_found(response)
        self.assert_items_are_listed(response, [center1.name])
        self.assert_items_are_not_listed(response, [center2.name, center3.name])

    def test_practice_center_details_should_display_practice_center_details(self):
        self.assert_item_details_are_displayed([
            (center1.id, center1.name),
            (center2.id, center2.name),
            (center3.id, center3.name),
        ])

    def test_practice_center_details__without_practice_center_should_respond_not_found(self):
        self.remove_practice_centers()
        self.assert_item_details_are_not_found([(center1.id, center1.name)])


if __name__ == "__main__":
    unittest.main()
