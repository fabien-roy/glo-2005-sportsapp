from app import conn
from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.models import PracticeCenter
from app.practice_centers.repositories import PracticeCentersRepository
from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_practice_center_queries import MySQLPracticeCentersQuery
from app.repositories.mysql_tables import MySQLPracticeCentersTable
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository


class MySQLPracticeCentersRepository(PracticeCentersRepository):
    # TODO : Inject in repositories
    climate_repository = MySQLClimatesRepository()
    recommendation_repository = MySQLRecommendationsRepository()

    def get_all(self, form=None):
        all_practice_centers = []

        try:
            with conn.cursor() as cur:
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
            with conn.cursor() as cur:
                query = MySQLPracticeCentersQuery().get(practice_center_id)
                cur.execute(query)

                # TODO : Use fetchone (causes integer error)
                for practice_center_cur in cur.fetchall():
                    climates = self.climate_repository.get_all_for_practice_center(practice_center_id)
                    recommendations = self.recommendation_repository.get_all_for_practice_center(practice_center_id)
                    practice_center = self.build_practice_center(practice_center_cur, climates, recommendations)
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
            with conn.cursor() as cur:
                query = MySQLPracticeCentersQuery().add()
                cur.execute(query, (practice_center.name, practice_center.email, practice_center.web_site,
                                    practice_center.phone_number))

                conn.commit()

                practice_center.id = cur.lastrowid

                for climate in practice_center.climates:
                    self.climate_repository.add_to_practice_center(climate, practice_center)
        finally:
            cur.close()
