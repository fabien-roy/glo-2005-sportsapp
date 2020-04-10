from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_shop_filters import MySQLShopsFilter
from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLShopsTable

all_fields_to_add = (MySQLShopsTable.name_col +
                     ', ' + MySQLShopsTable.email_col +
                     ', ' + MySQLShopsTable.phone_number_col +
                     ', ' + MySQLShopsTable.web_site_col)

all_fields = (MySQLShopsTable.id_col + ', ' + all_fields_to_add)

select_all_operation = ('SELECT ' + all_fields + ' FROM ' + MySQLShopsTable.table_name)


class MySQLShopsQuery(MySQLQuery):
    def get(self, shop_id):
        filters = [MySQLFilter.filter_equal(MySQLShopsTable.id_col, shop_id)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = MySQLShopsFilter().build_filters(form)

        orders = [MySQLShopsTable.name_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = ('INSERT INTO ' + MySQLShopsTable.table_name +
                     '(' + all_fields_to_add + ') VALUES (%s, %s, %s, %s)')

        return self.build_query(operation)
