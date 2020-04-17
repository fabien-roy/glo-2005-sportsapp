from app.recommendations.repositories import RecommendationRepository
from instance import injector
from instance.practice_centers.fakes import center1, center2, center3
from instance.recommendations.fakes import sport2_recommendation1, sport1_recommendation1, \
    sport2_recommendation2, sport3_recommendation1, center1_recommendation1, \
    center3_recommendation1, center2_recommendation2, center2_recommendation1, \
    center3_recommendation2
from instance.sports.fakes import sport1, sport2, sport3

recommendation_repository = injector.get(RecommendationRepository)


def db_populate_with_recommendations():
    recommendation_repository.add_for_sport(sport1_recommendation1, sport1)
    recommendation_repository.add_for_sport(sport2_recommendation1, sport2)
    recommendation_repository.add_for_sport(sport2_recommendation2, sport2)
    recommendation_repository.add_for_sport(sport3_recommendation1, sport3)

    recommendation_repository.add_for_practice_center(center1_recommendation1, center1)
    recommendation_repository.add_for_practice_center(center2_recommendation1, center2)
    recommendation_repository.add_for_practice_center(center2_recommendation2, center2)
    recommendation_repository.add_for_practice_center(center3_recommendation1, center3)
    recommendation_repository.add_for_practice_center(center3_recommendation2, center3)
