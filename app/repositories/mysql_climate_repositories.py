from app import conn
from app.climates.models import Climate
from app.climates.repositories import ClimatesRepository

from app.repositories.mysql_climate_queries import MySQLClimatesQuery


class MySQLClimatesRepository(ClimatesRepository):
    def get_all_for_sport(self, sport_id):
        query = MySQLClimatesQuery().get_all_for_sport(sport_id)
        return self.get_all_for_type(query)

    def get_all_for_practice_center(self, practice_center_id):
        query = MySQLClimatesQuery().get_all_for_practice_center(practice_center_id)
        return self.get_all_for_type(query)

    def get_all_for_type(self, query):
        climates = []

        try:
            with conn.cursor() as cur:
                cur.execute(query)

                for climate_cur in cur.fetchall():
                    climates.append(self.build_climate(climate_cur))
        finally:
            cur.close()

        return climates

    @staticmethod
    def build_climate(cur):
        return Climate(cur[MySQLClimatesQuery.fake_name_col])

    def add(self, climate):
        try:
            with conn.cursor() as cur:
                query = MySQLClimatesQuery().add()
                cur.execute(query, climate.name)

                conn.commit()
        finally:
            cur.close()

    def add_to_sport(self, climate, sport):
        query = MySQLClimatesQuery().add_for_sport()
        return self.add_to_type(query, climate.name, sport.id)

    def add_to_practice_center(self, climate, practice_center):
        query = MySQLClimatesQuery().add_for_practice_center()
        return self.add_to_type(query, climate.name, practice_center.id)

    @staticmethod
    def add_to_type(query, climate_name, type_id):
        try:
            with conn.cursor() as cur:
                cur.execute(query, (climate_name, type_id))

                conn.commit()
        finally:
            cur.close()
