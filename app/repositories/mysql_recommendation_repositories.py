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
