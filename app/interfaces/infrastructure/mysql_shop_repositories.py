from injector import inject

from app.announces.repositories import AnnouncesRepository
from app.database import Database
from app.repositories.mysql_shop_queries import MySQLShopsQuery
from app.repositories.mysql_tables import MySQLShopsTable
from app.shops.exceptions import ShopNotFoundException
from app.shops.models import Shop
from app.shops.repositories import ShopsRepository


class MySQLShopsRepository(ShopsRepository):
    @inject
    def __init__(self, database: Database, announces_repository: AnnouncesRepository):
        self.database = database
        self.announces_repository = announces_repository

    def get_all(self, form=None):
        all_shops = []

        try:
            with self.database.connect().cursor() as cur:
                query = MySQLShopsQuery().get_all(form)
                cur.execute(query)

                for shop_cur in cur.fetchall():
                    shop = self.build_shop(shop_cur)
                    all_shops.append(shop)
        finally:
            cur.close()

        return all_shops

    def get(self, shop_id):
        shop = None

        try:
            with self.database.connect().cursor() as cur:
                query = MySQLShopsQuery().get(shop_id)
                cur.execute(query)

                for shop_cur in cur.fetchall():
                    announces = self.announces_repository.get_all_for_shop(shop_id)
                    shop = self.build_shop(shop_cur, announces)
        finally:
            cur.close()

        if shop is None:
            raise ShopNotFoundException

        return shop

    @staticmethod
    def build_shop(cur, announces=None):
        return Shop(cur[MySQLShopsTable.id_col],
                    cur[MySQLShopsTable.name_col],
                    cur[MySQLShopsTable.email_col],
                    cur[MySQLShopsTable.phone_number_col],
                    cur[MySQLShopsTable.web_site_col],
                    announces)

    def add(self, shop):
        try:
            with self.database.connect().cursor() as cur:
                query = MySQLShopsQuery().add()
                cur.execute(query, (shop.name, shop.email, shop.phone_number, shop.web_site))

                self.database.connect().commit()

                shop.id = cur.lastrowid
        finally:
            cur.close()
