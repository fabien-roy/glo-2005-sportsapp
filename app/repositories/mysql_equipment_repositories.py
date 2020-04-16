from injector import inject

from app.announces.repositories import AnnouncesRepository
from app.database import Database
from app.equipments.exceptions import EquipmentNotFoundException
from app.equipments.models import Equipment
from app.equipments.repositories import EquipmentsRepository
from app.repositories.mysql_equipment_queries import MySQLEquipmentsQuery
from app.repositories.mysql_tables import MySQLEquipmentsTable


class MySQLEquipmentsRepository(EquipmentsRepository):
    @inject
    def __init__(self, database: Database, announces_repository: AnnouncesRepository):
        self.database = database
        self.announces_repository = announces_repository

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

            for equipment_cur in cur.fetchall():
                announces = self.announces_repository.get_all_for_equipment(equipment_id)
                equipment = self.build_equipment(equipment_cur, announces)
        finally:
            cur.close()

        if equipment is None:
            raise EquipmentNotFoundException

        return equipment

    @staticmethod
    def build_equipment(cur, announces=None):
        return Equipment(cur[MySQLEquipmentsTable.id_col],
                         cur[MySQLEquipmentsTable.name_col],
                         cur[MySQLEquipmentsTable.category_col],
                         cur[MySQLEquipmentsTable.description_col],
                         announces)

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
