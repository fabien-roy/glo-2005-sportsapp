from injector import inject

from app.practice_centers.repositories import PracticeCenterRepository
from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationRepository
from app.sports.repositories import SportRepository
from instance.resources.helpers import read_elements, sport_recommendations_csv, \
    practice_center_recommendations_csv


class RecommendationPopulationService:
    @inject
    def __init__(self, recommendation_repository: RecommendationRepository,
                 sport_repository: SportRepository,
                 practice_center_repository: PracticeCenterRepository):
        self.recommendation_repository = recommendation_repository
        self.sport_repository = sport_repository
        self.practice_center_repository = practice_center_repository

    def db_populate(self):
        for recommendation, practice_center_id in self.read_sport_recommendations():
            self.recommendation_repository.add_to_sport(recommendation, practice_center_id)

        for recommendation, practice_center_id in self.read_practice_center_recommendations():
            self.recommendation_repository.add_to_practice_center(recommendation,
                                                                  practice_center_id)

    def read_sport_recommendations(self):
        return read_elements(sport_recommendations_csv(), self.build_sport_recommendation)

    def read_practice_center_recommendations(self):
        return read_elements(practice_center_recommendations_csv(),
                             self.build_practice_center_recommendation)

    def build_sport_recommendation(self, row):
        sport = self.sport_repository.get_by_name(row[1])
        return Recommendation(recommendation_id=None, item_id=None, username=row[0], comment=row[2],
                              note=row[3], name=None), sport.id

    def build_practice_center_recommendation(self, row):
        practice_center = self.practice_center_repository.get_by_name(row[1])
        return Recommendation(recommendation_id=None, item_id=None, username=row[0], comment=row[2],
                              note=row[3], name=None), practice_center.id
