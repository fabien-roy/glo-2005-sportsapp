from injector import inject

from app.database import Database
from app.equipments.exceptions import EquipmentNotFoundException
from app.equipments.models import Equipment
from app.equipments.repositories import EquipmentsRepository
from app.repositories.mysql_equipment_queries import MySQLEquipmentsQuery
from app.repositories.mysql_tables import MySQLEquipmentsTable


class MySQLEquipmentsRepository(EquipmentsRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_all(self, form=None):
        all_equipments = []

        try:
            with self.database.connect().cursor() as cur:
                query = MySQLEquipmentsQuery().get_all(form)
                cur.execute(query)

                for equipment_cur in cur.fetchall():
                    equipment = self.build_equipment(equipment_cur)
                    all_equipments.append(equipment)
        finally:
            cur.close()

        return all_equipments

    def get(self, equipment_id):
        equipment = None

        try:
            with self.database.connect().cursor() as cur:
                query = MySQLEquipmentsQuery().get(equipment_id)
                cur.execute(query)

        finally:
            cur.close()

        if equipment is None:
            raise EquipmentNotFoundException

        return equipment

    @staticmethod
    def build_equipment(cur):
        return Equipment(cur[MySQLEquipmentsTable.id_col], cur[MySQLEquipmentsTable.name_col],
                         cur[MySQLEquipmentsTable.category_col],
                         cur[MySQLEquipmentsTable.description_col])

    def add(self, equipment):
        try:
            with self.database.connect().cursor() as cur:
                query = MySQLEquipmentsQuery().add()
                cur.execute(query, (equipment.category, equipment.name,
                                    equipment.description))

                self.database.connect().commit()

                equipment.id = cur.lastrowid

        finally:
            cur.close()
