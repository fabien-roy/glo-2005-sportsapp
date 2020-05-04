from datetime import datetime

from injector import inject

from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationRepository


class RecommendationService:
    @inject
    def __init__(self, recommendation_repository: RecommendationRepository):
        self.recommendation_repository = recommendation_repository

    def add_to_sport(self, username, sport, form):
        recommendation = self.create_recommendation(username, sport, form)
        self.recommendation_repository.add_to_sport(recommendation, sport.id)

    def add_to_practice_center(self, username, practice_center, form):
        recommendation = self.create_recommendation(username, practice_center, form)
        self.recommendation_repository.add_to_practice_center(recommendation, practice_center.id)

    @staticmethod
    def create_recommendation(username, sport, form):
        return Recommendation(None, sport.id, username, form.comment.data, form.note.data, sport.id,
                              datetime.now())
