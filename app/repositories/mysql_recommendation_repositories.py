import datetime

from app import conn
from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationsRepository

# TODO : Test correctly RecommendationsRepository

class MySQLRecommendationsRepository(RecommendationsRepository):
    table_name = 'recommendations'

    id_col = 'id'
    username_col = 'username'
    comment_col = 'comment'
    note_col = 'note'
    date_col = 'date'

    # TODO : Info about other tables is duplicated to avoid circular dependency. That could be improved.
    sport_recommendations_table_name = 'sport_recommendations'
    sport_recommendations_recommendation_id_col = 'recommendation_id'
    practice_center_recommendations_table_name = 'practice_center_recommendations'
    practice_center_recommendations_recommendation_id_col = 'recommendation_id'

    def get(self, recommendation_id):
        recommendation = None

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.username_col + ', ' + self.comment_col + ', ' +
                       self.note_col + ', ' + self.date_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.id_col + ' = %s;')
                cur.execute(sql, recommendation_id)

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
                sql = ('SELECT ' + self.id_col + ', ' + self.username_col + ', ' + self.comment_col + ', ' +
                       self.note_col + ', ' + self.date_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.username_col + ' = %s'
                       ' AND ' + self.id_col + ' IN (' +
                       '   SELECT ' + self.sport_recommendations_recommendation_id_col +
                       '   FROM ' + self.sport_recommendations_table_name +
                       ');')
                cur.execute(sql, username)

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
                sql = ('SELECT ' + self.id_col + ', ' + self.username_col + ', ' + self.comment_col + ', ' +
                       self.note_col + ', ' + self.date_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.username_col + ' = %s'
                                                       ' AND ' + self.id_col + ' IN (' +
                       '   SELECT ' + self.practice_center_recommendations_recommendation_id_col +
                       '   FROM ' + self.practice_center_recommendations_table_name +
                       ');')
                cur.execute(sql, username)

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
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.username_col + ', ' + self.comment_col + ', ' + self.note_col + ', ' +
                       self.date_col + ')' +
                       ' VALUES (%s, %s, %s, %s);')
                cur.execute(sql, (recommendation.username, recommendation.comment, recommendation.note,
                                  recommendation.date))

                conn.commit()

                recommendation.id = cur.lastrowid
        finally:
            cur.close()

        return cur.lastrowid
