from injector import inject

from app.manufacturers.infrastructure.tables import MySQLManufacturerTable as Manufacturers
from app.manufacturers.models import Manufacturer
from app.manufacturers.repositories import ManufacturerRepository
from app.manufacturers.infrastructure.queries import MySQLManufacturerQuery as Query
from app.interfaces.database import Database


class MySQLManufacturerRepository(ManufacturerRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_by_name(self, name):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_by_name(name)
                cur.execute(query)

                for manufacturer_cur in cur.fetchall():
                    return self.build_manufacturer(manufacturer_cur)
        finally:
            cur.close()

    @staticmethod
    def build_manufacturer(cur):
        return Manufacturer(cur[Manufacturers.id_col],
                            cur[Manufacturers.name_col])

    def add(self, manufacturer):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().add()
                cur.execute(query, manufacturer.name)

                self.database.connect().commit()

                manufacturer.id = cur.lastrowid

        finally:
            cur.close()
