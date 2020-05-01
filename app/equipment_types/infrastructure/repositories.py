from injector import inject

from app.equipment_types.repositories import EquipmentTypeRepository
from app.equipment_types.infrastructure.queries import MySQLCategoryQuery as Query
from app.interfaces.database import Database


class MySQLEquipmentTypeRepository(EquipmentTypeRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def add(self, equipment_type):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().add()
                cur.execute(query, equipment_type.name)

                self.database.connect().commit()

                equipment_type.id = cur.lastrowid

        finally:
            cur.close()
