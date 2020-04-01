import datetime

from app import conn
from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationsRepository

from app.repositories.mysql_recommendation_queries import MySQLRecommendationQuery
from app.repositories.mysql_tables import MySQLRecommendationsTable


# TODO : Test correctly RecommendationsRepository
class MySQLRecommendationsRepository(RecommendationsRepository):

    def get_all_for_sport(self, sport_id):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_all_for_sport(sport_id)
                cur.execute(query)

                for recommendation_cur in cur.fetchall():
                    recommendations.append(self.build_recommendation(recommendation_cur))
        finally:
            cur.close()

        return recommendations

    def get_all_for_practice_center(self, practice_center_id):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_all_for_practice_center(practice_center_id)
                cur.execute(query)

                for recommendation_cur in cur.fetchall():
                    recommendations.append(self.build_recommendation(recommendation_cur))
        finally:
            cur.close()

        return recommendations

    def get_all_for_sport_and_user(self, username):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_all_for_sport_and_user(username)
                cur.execute(query)

                for recommendation_cur in cur.fetchall():
                    recommendations.append(self.build_recommendation(recommendation_cur))
        finally:
            cur.close()

        return recommendations

    def get_all_for_practice_center_and_user(self, username):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_all_for_practice_center_and_user(username)
                cur.execute(query)

                for recommendation_cur in cur.fetchall():
                    recommendations.append(self.build_recommendation(recommendation_cur))
        finally:
            cur.close()

        return recommendations

    @staticmethod
    def build_recommendation(cur):
        return Recommendation(cur[MySQLRecommendationsTable.id_col],
                              cur[MySQLRecommendationQuery.item_id_fake_col],
                              cur[MySQLRecommendationsTable.username_col],
                              cur[MySQLRecommendationsTable.comment_col],
                              cur[MySQLRecommendationsTable.note_col],
                              cur[MySQLRecommendationQuery.name_fake_col],
                              cur[MySQLRecommendationsTable.date_col])

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
