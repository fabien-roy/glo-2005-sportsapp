import datetime

from app import conn
from app.recommendations.repositories import RecommendationRepository


class MySQLRecommendationRepository(RecommendationRepository):
    table_name = 'recommendations'

    comment_col = 'comment'
    note_col = 'note'
    date_col = 'date'

    def add(self, recommendation):
        try:
            recommendation.date = datetime.datetime.now()

            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.comment_col + ', ' + self.note_col + ', ' + self.date_col + ')' +
                       ' VALUES (%s, %s, %s);')
                cur.execute(sql, (recommendation.comment, recommendation.note, recommendation.date))

                conn.commit()
        finally:
            cur.close()

        return cur.lastrowid
