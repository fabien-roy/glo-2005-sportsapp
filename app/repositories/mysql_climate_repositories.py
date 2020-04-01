from app import conn
from app.climates.repositories import ClimatesRepository

from app.repositories.mysql_climate_queries import MySQLClimatesQuery


# TODO : test climates repo
class MySQLClimatesRepository(ClimatesRepository):
    def get_all_for_sport(self, sport_id):
        climates = []

        try:
            with conn.cursor() as cur:
                query = MySQLClimatesQuery().get_all_for_sport(sport_id)
                cur.execute(query)

                for climate_cur in cur.fetchall():
                    climates.append(self.build_climate(climate_cur))
        finally:
            cur.close()

        return climates

    def get_all_for_practice_center(self, sport_id):
        climates = []

        try:
            with conn.cursor() as cur:
                query = MySQLClimatesQuery().get_all_for_practice_center(sport_id)
                cur.execute(query)

                for climate_cur in cur.fetchall():
                    climates.append(self.build_climate(climate_cur))
        finally:
            cur.close()

        return climates

    @staticmethod
    def build_climate(climate_cur):
        pass

    def add(self, climate):
        try:
            with conn.cursor() as cur:
                query = MySQLClimatesQuery().add()
                cur.execute(query, climate.name)

                conn.commit()
        finally:
            cur.close()

    def add_to_sport(self, climate, sport):
        try:
            with conn.cursor() as cur:
                query = MySQLClimatesQuery().add_for_sport()
                cur.execute(query, (climate.name, sport.id))

                conn.commit()
        finally:
            cur.close()

    def add_to_practice_center(self, climate, practice_center):
        try:
            with conn.cursor() as cur:
                query = MySQLClimatesQuery().add_for_practice_center()
                cur.execute(query, (climate.name, practice_center.id))

                conn.commit()
        finally:
            cur.close()
