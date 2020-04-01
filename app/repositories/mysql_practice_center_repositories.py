from app import conn
from app.climates.models import Climate
from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.models import PracticeCenter
from app.practice_centers.repositories import PracticeCentersRepository
from app.repositories.mysql_practice_center_queries import MySQLPracticeCentersQuery
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository


class MySQLPracticeCenterClimateRepository:
    table_name = 'practice_center_climates'

    practice_center_id_col = 'practice_center_id'
    climate_name_col = 'climate_name'

    def get_climates(self, practice_center_id):
        climates = []

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.climate_name_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.practice_center_id_col + ' = %s;')
                cur.execute(sql, practice_center_id)

                for climate_cur in cur.fetchall():
                    climate = Climate(climate_cur[self.climate_name_col])
                    climates.append(climate)
        finally:
            cur.close()

        return climates

    def add(self, practice_center, climate):
        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.practice_center_id_col + ', ' + self.climate_name_col + ')' +
                       ' VALUES (%s, %s);')
                cur.execute(sql, (practice_center.id, climate.name))

                conn.commit()
        finally:
            cur.close()


class MySQLPracticeCenterRecommendationRepository:
    table_name = 'practice_center_recommendations'

    practice_center_id_col = 'practice_center_id'
    recommendation_id_col = 'recommendation_id'

    # TODO : Inject in repositories
    recommendation_repository = MySQLRecommendationsRepository()

    def get_recommendations(self, practice_center_id):
        return self.recommendation_repository.get_practice_center_recommendations(practice_center_id)

    def add(self, practice_center_id, recommendation):
        self.recommendation_repository.add(recommendation)

        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.practice_center_id_col + ', ' + self.recommendation_id_col + ')' +
                       ' VALUES (%s, %s);')
                cur.execute(sql, (practice_center_id, recommendation.id))

                conn.commit()
        finally:
            cur.close()


class MySQLPracticeCentersRepository(PracticeCentersRepository):

    # TODO : Inject in repositories
    practice_center_climate_repository = MySQLPracticeCenterClimateRepository()
    practice_center_recommendation_repository = MySQLPracticeCenterRecommendationRepository()

    def get_all(self, form=None):
        all_practice_centers = []

        try:
            with conn.cursor() as cur:
                query = MySQLPracticeCentersQuery.query().get_all(form)
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
                query = MySQLPracticeCentersQuery.query().get(practice_center_id)
                cur.execute(query)

                # TODO : Use fetchone (causes integer error)
                for practice_center_cur in cur.fetchall():
                    climates = self.practice_center_climate_repository.get_climates(practice_center_id)
                    recommendations = self.practice_center_recommendation_repository.get_recommendations(
                        practice_center_id)
                    practice_center = self.build_practice_center(practice_center_cur, climates, recommendations)
        finally:
            cur.close()

        if practice_center is None:
            raise PracticeCenterNotFoundException

        return practice_center

    @staticmethod
    def build_practice_center(cur, climates=None, recommendations=None):
        return PracticeCenter(cur[MySQLPracticeCentersQuery.id_col],
                              cur[MySQLPracticeCentersQuery.name_col],
                              cur[MySQLPracticeCentersQuery.email_col],
                              cur[MySQLPracticeCentersQuery.web_site_col],
                              cur[MySQLPracticeCentersQuery.phone_number_col],
                              climates,
                              recommendations)

    def add(self, practice_center):
        try:
            with conn.cursor() as cur:
                query = MySQLPracticeCentersQuery().add_practice_center()
                cur.execute(query, (practice_center.name, practice_center.email, practice_center.web_site,
                                    practice_center.phone_number))

                conn.commit()

                practice_center.id = cur.lastrowid

                for climate in practice_center.climates:
                    self.practice_center_climate_repository.add(practice_center, climate)
        finally:
            cur.close()

    def add_recommendation(self, practice_center_id, recommendation):
        self.practice_center_recommendation_repository.add(practice_center_id, recommendation)
