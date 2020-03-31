import datetime

from app import conn
from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationsRepository

# TODO : Test correctly RecommendationsRepository
from app.repositories.mysql_recommendation_queries import MySQLRecommendationQuery


class MySQLRecommendationsRepository(RecommendationsRepository):
    table_name = 'recommendations'

    id_col = 'id'
    username_col = 'username'
    comment_col = 'comment'
    note_col = 'note'
    date_col = 'date'

    sport_recommendations_table_name = 'sport_recommendations'
    sport_recommendations_recommendation_id_col = 'recommendation_id'
    practice_center_recommendations_table_name = 'practice_center_recommendations'
    practice_center_recommendations_recommendation_id_col = 'recommendation_id'

    def get(self, recommendation_id):
        recommendation = None

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get(recommendation_id)
                cur.execute(query)

                # TODO : Use fetchone (causes integer error)
                for recommendation_cur in cur.fetchall():
                    recommendation = Recommendation(recommendation_id,
                                                    recommendation_cur[self.username_col],
                                                    recommendation_cur[self.comment_col],
                                                    recommendation_cur[self.note_col],
                                                    recommendation_cur[self.date_col])
        finally:
            cur.close()

        return recommendation

    def get_sport_recommendations(self, username):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_sports(username)
                cur.execute(query)

                # TODO : Use fetchone (causes integer error)
                for recommendation_cur in cur.fetchall():
                    recommendation = Recommendation(recommendation_cur[self.id_col],
                                                    recommendation_cur[self.username_col],
                                                    recommendation_cur[self.comment_col],
                                                    recommendation_cur[self.note_col],
                                                    recommendation_cur[self.date_col])
                    recommendations.append(recommendation)
        finally:
            cur.close()

        return recommendations

    def get_practice_center_recommendations(self, username):
        recommendations = []

        try:
            with conn.cursor() as cur:
                query = MySQLRecommendationQuery().get_practice_centers(username)
                cur.execute(query)

                # TODO : Use fetchone (causes integer error)
                for recommendation_cur in cur.fetchall():
                    recommendation = Recommendation(recommendation_cur[self.id_col],
                                                    recommendation_cur[self.username_col],
                                                    recommendation_cur[self.comment_col],
                                                    recommendation_cur[self.note_col],
                                                    recommendation_cur[self.date_col])
                    recommendations.append(recommendation)
        finally:
            cur.close()

        return recommendations

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
