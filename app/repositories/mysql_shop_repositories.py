from app import conn
from app.repositories.mysql_shop_queries import MySQLShopsQuery
from app.shops.exceptions import ShopNotFoundException
from app.shops.models import Shop
from app.shops.repositories import ShopsRepository


class MySQLShopsRepository(ShopsRepository):
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
        return Shop(cur[MySQLShopsQuery.id_col],
                    cur[MySQLShopsQuery.name_col],
                    cur[MySQLShopsQuery.email_col],
                    cur[MySQLShopsQuery.phone_number_col],
                    cur[MySQLShopsQuery.web_site_col])

    def add(self, shop):
        try:
            with conn.cursor() as cur:
                query = MySQLShopsQuery().add()
                cur.execute(query, (shop.id, shop.name, shop.email, shop.phone_number, shop.web_site))

                conn.commit()

                shop.id = cur.lastrowid
        finally:
            cur.close()
