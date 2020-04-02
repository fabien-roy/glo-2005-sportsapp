from app import conn
from app.repositories.mysql_shop_queries import MySQLShopsQuery
from app.repositories.mysql_tables import MySQLShopsTable
from app.shops.exceptions import ShopNotFoundException
from app.shops.models import Shop
from app.shops.repositories import ShopsRepository


class MySQLShopsRepository(ShopsRepository):
    def get_all(self, form=None):
        all_shops = []

        try:
            with conn.cursor() as cur:
                query = MySQLShopsQuery().get_all(form)
                cur.execute(query)

                for sport_cur in cur.fetchall():
                    sport = self.build_shop(sport_cur)
                    all_shops.append(sport)
        finally:
            cur.close()

        return all_shops

    def get(self, shop_id):
        shop = None

        try:
            with conn.cursor() as cur:
                query = MySQLShopsQuery().get(shop_id)
                cur.execute(query)

                # TODO : Use fetchone (causes integer error)
                for shop_cur in cur.fetchall():
                    shop = self.build_shop(shop_cur)
        finally:
            cur.close()

        if shop is None:
            raise ShopNotFoundException

        return shop

    @staticmethod
    def build_shop(cur):
        return Shop(cur[MySQLShopsTable.id_col],
                    cur[MySQLShopsTable.name_col],
                    cur[MySQLShopsTable.email_col],
                    cur[MySQLShopsTable.phone_number_col],
                    cur[MySQLShopsTable.web_site_col])

    def add(self, shop):
        try:
            with conn.cursor() as cur:
                query = MySQLShopsQuery().add()
                cur.execute(query, (shop.name, shop.email, shop.phone_number, shop.web_site))

                conn.commit()

                shop.id = cur.lastrowid
        finally:
            cur.close()
