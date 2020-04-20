from injector import inject

from app.announces.repositories import AnnounceRepository
from app.equipments.exceptions import EquipmentNotFoundException
from app.equipments.models import Equipment
from app.equipments.repositories import EquipmentRepository
from app.equipments.infrastructure.queries import MySQLEquipmentQuery as Query
from app.equipments.infrastructure.tables import MySQLEquipmentTable as Equipments
from app.interfaces.database import Database


class MySQLEquipmentRepository(EquipmentRepository):
    @inject
    def __init__(self, database: Database, announce_repository: AnnounceRepository):
        self.database = database
        self.announce_repository = announce_repository

    def get_all(self, form=None):
        all_equipments = []

        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_all(form)
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
                query = Query().get(equipment_id)
                cur.execute(query)

            for equipment_cur in cur.fetchall():
                announces = self.announce_repository.get_all_for_equipment(equipment_id)
                equipment = self.build_equipment(equipment_cur, announces)
        finally:
            cur.close()

        if equipment is None:
            raise EquipmentNotFoundException

        return equipment

    @staticmethod
    def build_equipment(cur, announces=None):
        return Equipment(cur[Equipments.id_col],
                         cur[Equipments.category_col],
                         cur[Equipments.name_col],
                         cur[Equipments.description_col],
                         announces)

    def add(self, equipment):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().add()
                cur.execute(query, (equipment.category, equipment.name,
                                    equipment.description))

                self.database.connect().commit()

                equipment.id = cur.lastrowid

        finally:
            cur.close()
