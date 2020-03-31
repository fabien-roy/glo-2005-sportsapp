import datetime

from app import conn
from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationsRepository

# TODO : Test correctly RecommendationsRepository
from app.repositories.mysql_recommendation_queries import MySQLRecommendationQuery


class MySQLRecommendationsRepository(RecommendationsRepository):
    def get_sport_recommendations(self, sport_id):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_sport_recommendations(sport_id)
                cur.execute(query)

                for recommendation_cur in cur.fetchall():
                    recommendations.append(self.build_recommendation(recommendation_cur))
        finally:
            cur.close()

        return recommendations

    def get_practice_center_recommendations(self, practice_center_id):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_practice_center_recommendations(practice_center_id)
                cur.execute(query)

                for recommendation_cur in cur.fetchall():
                    recommendations.append(self.build_recommendation(recommendation_cur))
        finally:
            cur.close()

        return recommendations

    def get_sport_recommendations_for_user(self, username):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_sport_recommendations_for_user(username)
                cur.execute(query)

                for recommendation_cur in cur.fetchall():
                    recommendations.append(self.build_recommendation(recommendation_cur))
        finally:
            cur.close()

        return recommendations

    def get_practice_center_recommendations_for_user(self, username):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_practice_center_recommendations_for_user(username)
                cur.execute(query)

                for recommendation_cur in cur.fetchall():
                    recommendations.append(self.build_recommendation(recommendation_cur))
        finally:
            cur.close()

        return recommendations

    @staticmethod
    def build_recommendation(cur):
        return Recommendation(cur[MySQLRecommendationQuery.id_col],
                              cur[MySQLRecommendationQuery.item_id_fake_col],
                              cur[MySQLRecommendationQuery.username_col],
                              cur[MySQLRecommendationQuery.comment_col],
                              cur[MySQLRecommendationQuery.note_col],
                              cur[MySQLRecommendationQuery.name_fake_col],
                              cur[MySQLRecommendationQuery.date_col])

    def add(self, recommendation):
        try:
            recommendation.date = datetime.datetime.now()

            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().add()
                cur.execute(query, (recommendation.username, recommendation.comment, recommendation.note,
                                    recommendation.date))

                conn.commit()

                recommendation.id = cur.lastrowid
        finally:
            cur.close()

        return cur.lastrowid
