from injector import Module

from app.recommendations.infrastructure.repositories import MySQLRecommendationRepository
from app.recommendations.repositories import RecommendationRepository


class RecommendationModule(Module):
    def configure(self, binder):
        binder.bind(RecommendationRepository, to=MySQLRecommendationRepository)
