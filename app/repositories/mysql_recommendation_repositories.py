import datetime

from app import conn
from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationsRepository
from app.repositories.mysql_recommendation_queries import MySQLRecommendationQuery
from app.repositories.mysql_tables import MySQLRecommendationsTable


class MySQLRecommendationsRepository(RecommendationsRepository):

    def get_all_for_sport(self, sport_id):
        query = MySQLRecommendationQuery().get_all_for_sport(sport_id)
        return self.get_all(query)

    def get_all_for_practice_center(self, practice_center_id):
        query = MySQLRecommendationQuery().get_all_for_practice_center(practice_center_id)
        return self.get_all(query)

    def get_all_for_sport_and_user(self, username):
        query = MySQLRecommendationQuery().get_all_for_sport_and_user(username)
        return self.get_all(query)

    def get_all_for_practice_center_and_user(self, username):
        query = MySQLRecommendationQuery().get_all_for_practice_center_and_user(username)
        return self.get_all(query)

    def get_all(self, query):
        recommendations = []

        try:
            with conn.cursor() as cur:
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
        recommendation.date = datetime.datetime.now()
        query = MySQLRecommendationQuery().add()

        try:
            with conn.cursor() as cur:
                cur.execute(query, (recommendation.username, recommendation.comment, recommendation.note,
                                    recommendation.date))

                conn.commit()

                recommendation.id = cur.lastrowid
        finally:
            cur.close()

        return cur.lastrowid

    def add_for_sport(self, recommendation, sport):
        query = MySQLRecommendationQuery().add_to_sport()
        self.add_for_type(recommendation, query, sport.id)

    def add_for_practice_center(self, recommendation, practice_center):
        query = MySQLRecommendationQuery().add_to_practice_center()
        self.add_for_type(recommendation, query, practice_center.id)

    def add_for_type(self, recommendation, query, type_id):
        self.add(recommendation)

        try:
            with conn.cursor() as cur:
                cur.execute(query, (recommendation.id, type_id))

                conn.commit()
        finally:
            cur.close()
