from app import conn
from app.climates.models import Climate
from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.models import PracticeCenter
from app.practice_centers.repositories import PracticeCentersRepository
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
        recommendations = []

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.recommendation_id_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.practice_center_id_col + ' = %s;')
                cur.execute(sql, practice_center_id)

                # TODO : Solve n+1 problem
                for recommendation_cur in cur.fetchall():
                    recommendation = self.recommendation_repository.get(recommendation_cur[self.recommendation_id_col])
                    recommendations.append(recommendation)
        finally:
            cur.close()

        return recommendations

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
    table_name = 'practice_centers'

    id_col = 'id'
    name_col = 'name'
    email_col = 'email'
    web_site_col = 'web_site'
    phone_number_col = 'phone_number'

    practice_center_climate_repository = MySQLPracticeCenterClimateRepository()
    practice_center_recommendation_repository = MySQLPracticeCenterRecommendationRepository()

    def get_all(self):
        all_practice_centers = []

        try:
            with conn.cursor() as cur:
                cur.execute('SELECT ' + self.id_col + ', ' + self.name_col + ', ' + self.email_col + ', ' +
                            self.web_site_col + ', ' + self.phone_number_col +
                            ' FROM ' + self.table_name +
                            ' ORDER BY ' + self.name_col + ';')

                for practice_center_cur in cur.fetchall():
                    practice_center = PracticeCenter(practice_center_cur[self.id_col],
                                                     practice_center_cur[self.name_col],
                                                     practice_center_cur[self.email_col],
                                                     practice_center_cur[self.web_site_col],
                                                     practice_center_cur[self.phone_number_col])
                    all_practice_centers.append(practice_center)
        finally:
            cur.close()

        return all_practice_centers

    def get(self, practice_center_id):
        practice_center = None

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.id_col + ', ' + self.name_col + ', ' + self.email_col + ', ' +
                       self.web_site_col + ', ' + self.phone_number_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.id_col + ' = %s;')
                cur.execute(sql, practice_center_id)

                # TODO : Use fetchone (causes integer error)
                for practice_center_cur in cur.fetchall():
                    climates = self.practice_center_climate_repository.get_climates(practice_center_id)
                    recommendations = self.practice_center_recommendation_repository.get_recommendations(practice_center_id)
                    practice_center = PracticeCenter(practice_center_id,
                                                     practice_center_cur[self.name_col],
                                                     practice_center_cur[self.email_col],
                                                     practice_center_cur[self.web_site_col],
                                                     practice_center_cur[self.phone_number_col],
                                                     climates,
                                                     recommendations)
        finally:
            cur.close()

        if practice_center is None:
            raise PracticeCenterNotFoundException

        return practice_center

    def add(self, practice_center):
        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.name_col + ', ' + self.email_col + ', ' + self.web_site_col +
                       ', ' + self.phone_number_col + ')' +
                       ' VALUES (%s, %s, %s, %s);')
                cur.execute(sql, (practice_center.name, practice_center.email, practice_center.web_site,
                                  practice_center.phone_number))

                conn.commit()

                practice_center.id = cur.lastrowid

                for climate in practice_center.climates:
                    self.practice_center_climate_repository.add(practice_center, climate)
        finally:
            cur.close()

    def add_recommendation(self, practice_center_id, recommendation):
        self.practice_center_recommendation_repository.add(practice_center_id, recommendation)
