from injector import inject

from app.announces.repositories import AnnounceRepository
from app.interfaces.database import Database
from app.shops.exceptions import ShopNotFoundException
from app.shops.infrastructure.queries import MySQLShopQuery as Query
from app.shops.infrastructure.tables import MySQLShopTable as Shops
from app.shops.models import Shop
from app.shops.repositories import ShopRepository


class MySQLShopRepository(ShopRepository):
    @inject
    def __init__(self, database: Database, announces_repository: AnnounceRepository):
        self.database = database
        self.announces_repository = announces_repository

    def get_all(self, form=None, offset=None, per_page=None):
        all_shops = []

        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_all(form, offset, per_page)
                cur.execute(query)

                for shop_cur in cur.fetchall():
                    shop = self.build_shop(shop_cur)
                    all_shops.append(shop)
        finally:
            cur.close()

        return all_shops

    def get_count(self, form=None):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_count(form)
                cur.execute(query)

                for shop_cur in cur.fetchall():
                    return shop_cur[Query.fake_count_col]
        finally:
            cur.close()

        return 0

    def get(self, shop_id):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().get(shop_id)
                cur.execute(query)

                for shop_cur in cur.fetchall():
                    announces = self.announces_repository.get_all_for_shop(shop_id)
                    return self.build_shop(shop_cur, announces)
        finally:
            cur.close()

        raise ShopNotFoundException

    def get_by_name(self, name):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_by_name(name)
                cur.execute(query)

                for shop_cur in cur.fetchall():
                    return self.build_shop(shop_cur)
        finally:
            cur.close()

        raise ShopNotFoundException

    @staticmethod
    def build_shop(cur, announces=None):
        return Shop(cur[Shops.id_col],
                    cur[Shops.name_col],
                    cur[Shops.email_col],
                    cur[Shops.phone_number_col],
                    cur[Shops.web_site_col],
                    announces)

    def add(self, shop):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().add()
                cur.execute(query, (shop.name, shop.email, shop.phone_number, shop.web_site))

                self.database.connect().commit()

                shop.id = cur.lastrowid
        finally:
            cur.close()
