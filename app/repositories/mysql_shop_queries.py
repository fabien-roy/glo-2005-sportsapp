from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLShopsTable

all_fields_to_add = (MySQLShopsTable.name_col +
                     ', ' + MySQLShopsTable.email_col +
                     ', ' + MySQLShopsTable.phone_number_col +
                     ', ' + MySQLShopsTable.web_site_col)

all_fields = (MySQLShopsTable.id_col + ', ' + all_fields_to_add)

select_all_operation = ('SELECT ' + all_fields + ' FROM ' + MySQLShopsTable.table_name)


class MySQLShopsQuery(MySQLQuery):
    def get_all(self, form=None):
        operation = ('SELECT ' + MySQLShopsTable.id_col +
                     ', ' + MySQLShopsTable.name_col + ', ' + MySQLShopsTable.email_col + ', ' +
                     MySQLShopsTable.phone_number_col + ', ' + MySQLShopsTable.web_site_col +
                     ' FROM ' + MySQLShopsTable.table_name)

        if form is None:
            filters = None
        else:
            filters = []

            if form.name is not None:
                filters.append(self.filter_like(MySQLShopsTable.name_col, form.name.data))

        orders = [MySQLShopsTable.name_col]

        return self.build_query(operation, filters, orders)

    def get(self, shop_id):
        filters = [self.filter_equal(MySQLShopsTable.id_col, shop_id)]

        return self.build_query(select_all_operation, filters)

    def add(self):
        operation = ('INSERT INTO ' + MySQLShopsTable.table_name +
                     ' (' + all_fields_to_add + ')' +
                     ' VALUES (%s, %s, %s, %s)')

        return self.build_query(operation)
