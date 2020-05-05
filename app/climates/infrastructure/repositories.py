from injector import inject

from app.climates.infrastructure.tables import MySQLClimateTable
from app.climates.models import Climate
from app.climates.repositories import ClimateRepository

from app.climates.infrastructure.queries import MySQLClimateQuery as Query
from app.interfaces.database import Database


class MySQLClimateRepository(ClimateRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_all_for_sport(self, sport_id):
        query = Query().get_all_for_sport(sport_id)
        return self.get_all_for_type(query)

    def get_all_for_practice_center(self, practice_center_id):
        query = Query().get_all_for_practice_center(practice_center_id)
        return self.get_all_for_type(query)

    def get_all_for_type(self, query):
        climates = []

        try:
            with self.database.connect().cursor() as cur:
                cur.execute(query)

                for climate_cur in cur.fetchall():
                    climates.append(self.build_climate_for_type(climate_cur))
        finally:
            cur.close()

        return climates

    @staticmethod
    def build_climate_for_type(cur):
        return Climate(cur[Query.fake_name_col])

    def add(self, climate):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().add()
                cur.execute(query, climate.name)

                self.database.connect().commit()

                climate.id = cur.lastrowid
        finally:
            cur.close()

    def add_to_sport(self, climate, sport):
        query = Query().add_to_sport()
        return self.add_to_type(query, climate.name, sport.id)

    def add_to_practice_center(self, climate, practice_center):
        query = Query().add_for_practice_center()
        return self.add_to_type(query, climate.name, practice_center.id)

    def add_to_type(self, query, climate_name, type_id):
        try:
            with self.database.connect().cursor() as cur:
                cur.execute(query, (climate_name, type_id))

                self.database.connect().commit()
        finally:
            cur.close()
