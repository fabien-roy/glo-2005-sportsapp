from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLShopsTable


class MySQLShopsQuery(MySQLQuery):
    def get_all(self, form=None):
        operation = ('SELECT ' + MySQLShopsTable.id_col +
                     ', ' + MySQLShopsTable.name_col +
                     ', ' + MySQLShopsTable.email_col +
                     ', ' + MySQLShopsTable.phone_number_col +
                     ', ' + MySQLShopsTable.web_site_col +
                     ' FROM ' + MySQLShopsTable.table_name)

        # TODO : Search form for shops
        filters = []

        orders = [MySQLShopsTable.name_col]

        return self.build_query(operation, filters, orders)

    def get(self, shop_id):
        operation = ('SELECT ' + MySQLShopsTable.id_col +
                     ', ' + MySQLShopsTable.name_col +
                     ', ' + MySQLShopsTable.email_col +
                     ', ' + MySQLShopsTable.phone_number_col +
                     ', ' + MySQLShopsTable.web_site_col +
                     ' FROM ' + MySQLShopsTable.table_name)

        filters = [self.filter_equal(MySQLShopsTable.id_col, shop_id)]

        return self.build_query(operation, filters)

    def add(self):
        operation = ('INSERT INTO ' + MySQLShopsTable.table_name +
                     ' (' + MySQLShopsTable.id_col +
                     ', ' + MySQLShopsTable.name_col +
                     ', ' + MySQLShopsTable.email_col +
                     ', ' + MySQLShopsTable.phone_number_col +
                     ', ' + MySQLShopsTable.web_site_col + ')' +
                     ' VALUES (%s, %s, %s, %s, %s)')

        return self.build_query(operation)
