from instance.recommendations.fakes import sport1_recommendation1_user1, \
    sport2_recommendation1_user3
from tests.interfaces.test_basic import BasicTests


class RecommendationTests(BasicTests):

    def test_equals_with_non_announce_should_return_false(self):
        self.assertFalse(sport1_recommendation1_user1 == object)

    def test_equals_with_other_announce_should_return_false(self):
        self.assertFalse(sport1_recommendation1_user1 == sport2_recommendation1_user3)

    def test_equals_with_same_announce_should_return_true(self):
        self.assertTrue(sport1_recommendation1_user1 == sport1_recommendation1_user1)
