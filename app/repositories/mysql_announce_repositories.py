import datetime

from injector import inject

from app.announces.models import Announce
from app.announces.repositories import AnnouncesRepository
from app.database import Database
from app.repositories.mysql_announce_queries import MySQLAnnouncesQuery
from app.repositories.mysql_tables import MySQLAnnouncesTable


class MySQLAnnouncesRepository(AnnouncesRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_all_for_shop(self, shop_id):
        query = MySQLAnnouncesQuery().get_all_for_shop(shop_id)
        return self.get_all(query)

    def get_all_for_equipment(self, equipment_id):
        query = MySQLAnnouncesQuery().get_all_for_equipment(equipment_id)
        return self.get_all(query)

    def get_all(self, query):
        announces = []

        try:
            with self.database.connect().cursor() as cur:
                cur.execute(query)

                for announce_cur in cur.fetchall():
                    announces.append(self.build_announce(announce_cur))
        finally:
            cur.close()

        return announces

    @staticmethod
    def build_announce(cur):
        return Announce(cur[MySQLAnnouncesTable.id_col],
                        cur[MySQLAnnouncesTable.shop_id_col],
                        cur[MySQLAnnouncesTable.equipment_id_col],
                        cur[MySQLAnnouncesTable.state_col],
                        cur[MySQLAnnouncesTable.price_col],
                        cur[MySQLAnnouncesTable.date_col])

    def add(self, announce):
        announce.date = datetime.datetime.now()
        query = MySQLAnnouncesQuery().add()

        try:
            with self.database.connect().cursor() as cur:
                cur.execute(query, (announce.shop_id, announce.equipment_id, announce.state,
                                    announce.price, announce.date))

                self.database.connect().commit()

                announce.id = cur.lastrowid
        finally:
            cur.close()

        return cur.lastrowid
