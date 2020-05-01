from injector import inject

from app.recommendations.repositories import RecommendationRepository
from instance.practice_centers.fakes import center1, center2, center3
from instance.recommendations.fakes import sport2_recommendation1_user3, \
    sport1_recommendation1_user1, \
    sport2_recommendation2_user2, sport3_recommendation1_user1, center1_recommendation1_user1, \
    center3_recommendation1_user3, center2_recommendation2_user2, center2_recommendation1_user1, \
    center3_recommendation2_user1
from instance.sports.fakes import sport1, sport2, sport3


class RecommendationPopulationService:
    @inject
    def __init__(self, recommendation_repository: RecommendationRepository):
        self.recommendation_repository = recommendation_repository

    def db_populate(self):
        self.recommendation_repository.add_to_sport(sport1_recommendation1_user1, sport1.id)
        self.recommendation_repository.add_to_sport(sport2_recommendation1_user3, sport2.id)
        self.recommendation_repository.add_to_sport(sport2_recommendation2_user2, sport2.id)
        self.recommendation_repository.add_to_sport(sport3_recommendation1_user1, sport3.id)

        self.recommendation_repository.add_to_practice_center(center1_recommendation1_user1,
                                                              center1.id)
        self.recommendation_repository.add_to_practice_center(center2_recommendation1_user1,
                                                              center2.id)
        self.recommendation_repository.add_to_practice_center(center2_recommendation2_user2,
                                                              center2.id)
        self.recommendation_repository.add_to_practice_center(center3_recommendation1_user3,
                                                              center3.id)
        self.recommendation_repository.add_to_practice_center(center3_recommendation2_user1,
                                                              center3.id)
