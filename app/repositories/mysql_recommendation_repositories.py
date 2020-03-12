import datetime

from app import conn
from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationRepository


class MySQLRecommendationRepository(RecommendationRepository):
    table_name = 'recommendations'

    id_col = 'id'
    username_col = 'username'
    comment_col = 'comment'
    note_col = 'note'
    date_col = 'date'

    # TODO : Info about sport_recommendations table is duplicated to avoid circular dependency. That could be improved.
    sport_recommendations_table_name = 'sport_recommendations'

    sport_recommendations_sport_id_col = 'sport_id'

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
                       ' INNER JOIN ' + self.sport_recommendations_table_name + ' ON ' +
                       self.sport_recommendations_table_name + '.' + self.sport_recommendations_sport_id_col + ' = ' +
                       self.table_name + '.' + self.id_col +
                       ' WHERE ' + self.username_col + ' = %s;')
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
