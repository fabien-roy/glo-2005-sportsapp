import datetime

from injector import inject
from pymysql import MySQLError

from app.interfaces.database import Database
from app.recommendations.exceptions import OutOfBoundsNoteException
from app.recommendations.infrastructure.tables import MySQLRecommendationTable as Recommendations
from app.recommendations.infrastructure.queries import MySQLRecommendationQuery as Query
from app.recommendations.models import Recommendation
from app.recommendations.repositories import RecommendationRepository


class MySQLRecommendationRepository(RecommendationRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_all_for_sport(self, sport_id):
        query = Query().get_all_for_sport(sport_id)
        return self.get_all(query)

    def get_all_for_practice_center(self, practice_center_id):
        query = Query().get_all_for_practice_center(practice_center_id)
        return self.get_all(query)

    def get_all_for_sport_and_user(self, username):
        query = Query().get_all_for_sport_and_user(username)
        return self.get_all(query)

    def get_all_for_practice_center_and_user(self, username):
        query = Query().get_all_for_practice_center_and_user(username)
        return self.get_all(query)

    def get_all(self, query):
        recommendations = []

        try:
            with self.database.connect().cursor() as cur:
                cur.execute(query)

                for recommendation_cur in cur.fetchall():
                    recommendations.append(self.build_recommendation(recommendation_cur))
        finally:
            cur.close()

        return recommendations

    @staticmethod
    def build_recommendation(cur):
        return Recommendation(cur[Recommendations.id_col],
                              cur[Query.item_id_fake_col],
                              cur[Recommendations.username_col],
                              cur[Recommendations.comment_col],
                              cur[Recommendations.note_col],
                              cur[Query.name_fake_col],
                              cur[Recommendations.date_col])

    def add(self, recommendation):
        recommendation.date = datetime.datetime.now()
        query = Query().add()

        try:
            with self.database.connect().cursor() as cur:
                cur.execute(query, (recommendation.username, recommendation.comment,
                                    recommendation.note, recommendation.date))

                self.database.connect().commit()

                recommendation.id = cur.lastrowid
        except MySQLError as error:
            raise OutOfBoundsNoteException
        finally:
            cur.close()

        return cur.lastrowid

    def add_to_sport(self, recommendation, sport_id):
        query = Query().add_to_sport()
        self.add_to_type(recommendation, query, sport_id)

    def add_to_practice_center(self, recommendation, practice_center_id):
        query = Query().add_to_practice_center()
        self.add_to_type(recommendation, query, practice_center_id)

    def add_to_type(self, recommendation, query, type_id):
        self.add(recommendation)

        try:
            with self.database.connect().cursor() as cur:
                cur.execute(query, (recommendation.id, type_id))

                self.database.connect().commit()
        finally:
            cur.close()
