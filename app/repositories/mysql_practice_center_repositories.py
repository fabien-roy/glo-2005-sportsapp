from injector import inject

from app.climates.repositories import ClimatesRepository
from app.database import Database
from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.models import PracticeCenter
from app.practice_centers.repositories import PracticeCentersRepository
from app.recommendations.repositories import RecommendationsRepository
from app.repositories.mysql_practice_center_queries import MySQLPracticeCentersQuery
from app.repositories.mysql_tables import MySQLPracticeCentersTable


class MySQLPracticeCentersRepository(PracticeCentersRepository):
    @inject
    def __init__(self, database: Database, climates_repository: ClimatesRepository,
                 recommendations_repository: RecommendationsRepository):
        self.database = database
        self.climates_repository = climates_repository
        self.recommendations_repository = recommendations_repository

    def get_all(self, form=None):
        all_practice_centers = []

        try:
            with self.database.connect().cursor() as cur:
                query = MySQLPracticeCentersQuery().get_all(form)
                cur.execute(query)

                for practice_center_cur in cur.fetchall():
                    practice_center = self.build_practice_center(practice_center_cur)
                    all_practice_centers.append(practice_center)
        finally:
            cur.close()

        return all_practice_centers

    def get(self, practice_center_id):
        practice_center = None

        try:
            with self.database.connect().cursor() as cur:
                query = MySQLPracticeCentersQuery().get(practice_center_id)
                cur.execute(query)

                for practice_center_cur in cur.fetchall():
                    climates = self.climates_repository\
                        .get_all_for_practice_center(practice_center_id)
                    recommendations = self.recommendations_repository\
                        .get_all_for_practice_center(practice_center_id)
                    practice_center = self.build_practice_center(practice_center_cur, climates,
                                                                 recommendations)
        finally:
            cur.close()

        if practice_center is None:
            raise PracticeCenterNotFoundException

        return practice_center

    @staticmethod
    def build_practice_center(cur, climates=None, recommendations=None):
        return PracticeCenter(cur[MySQLPracticeCentersTable.id_col],
                              cur[MySQLPracticeCentersTable.name_col],
                              cur[MySQLPracticeCentersTable.email_col],
                              cur[MySQLPracticeCentersTable.web_site_col],
                              cur[MySQLPracticeCentersTable.phone_number_col],
                              climates,
                              recommendations)

    def add(self, practice_center):
        try:
            with self.database.connect().cursor() as cur:
                query = MySQLPracticeCentersQuery().add()
                cur.execute(query, (practice_center.name, practice_center.email,
                                    practice_center.web_site, practice_center.phone_number))

                self.database.connect().commit()

                practice_center.id = cur.lastrowid

                for climate in practice_center.climates:
                    self.climates_repository.add_to_practice_center(climate, practice_center)
        finally:
            cur.close()
