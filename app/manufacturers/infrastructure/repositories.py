from injector import inject

from app.manufacturers.repositories import ManufacturerRepository
from app.manufacturers.infrastructure.queries import MySQLManufacturerQuery as Query
from app.interfaces.database import Database


class MySQLManufacturerRepository(ManufacturerRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def add(self, manufacturer):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().add()
                cur.execute(query, manufacturer.name)

                self.database.connect().commit()

                manufacturer.id = cur.lastrowid

        finally:
            cur.close()
