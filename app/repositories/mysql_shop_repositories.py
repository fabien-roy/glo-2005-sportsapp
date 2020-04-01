from app import conn
from app.repositories.mysql_shop_queries import MySQLShopsQuery
from app.shops.repositories import ShopsRepository
from app.repositories.mysql_queries import build_query, filter_equal, filter_like


class MySQLShopsRepository(ShopsRepository):
    table_name = 'shops'

    id_col = 'id'
    location_id_col = 'location_id'
    name_col = 'name'
    email_col = 'email'
    phone_number_col = 'phone_number'
    web_site_col = 'web_site'

    def get(self, shop_id):
        operation = ('SELECT ' + self.id_col + ', ' + self.location_id_col + ', ' + self.name_col +
                     ', ' + self.email_col + ', ' + self.phone_number_col + ', ' + self.web_site_col +
                     ' FROM ' + self.table_name)

        filters = [filter_equal(self.id_col, shop_id)]

        return build_query(operation, filters)

    def add(self, shop):
        try:
            with conn.cursor() as cur:
                query = MySQLShopsQuery().add()
                cur.execute(query, (shop.id, shop.location, shop.name,
                                    shop.email, shop.phone_number, shop.web_site))

                conn.commit()

                shop.id = cur.lastrowid
        finally:
            cur.close()
