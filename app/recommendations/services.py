from datetime import datetime

from injector import inject

from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationRepository


# TODO : Test
class RecommendationService:
    @inject
    def __init__(self, recommendation_repository: RecommendationRepository):
        self.recommendation_repository = recommendation_repository

    def add_to_sport(self, username, sport, form):
        recommendation = self.create_recommendation(username, sport, form)
        self.recommendation_repository.add_to_sport(recommendation, sport.id)

    @staticmethod
    def create_recommendation(username, sport, form):
        return Recommendation(None, sport.id, username, form.data.comment, form.data.note, sport.id,
                              datetime.now())
