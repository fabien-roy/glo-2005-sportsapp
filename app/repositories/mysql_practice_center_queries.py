from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_practice_center_filters import MySQLPracticeCentersFilter
from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLPracticeCentersTable

all_fields_to_add = (MySQLPracticeCentersTable.name_col +
                     ', ' + MySQLPracticeCentersTable.email_col +
                     ', ' + MySQLPracticeCentersTable.web_site_col +
                     ', ' + MySQLPracticeCentersTable.phone_number_col)

all_fields = (MySQLPracticeCentersTable.id_col + ', ' + all_fields_to_add)

select_all_operation = ('SELECT ' + all_fields + ' FROM ' + MySQLPracticeCentersTable.table_name)


class MySQLPracticeCentersQuery(MySQLQuery):
    def get(self, practice_center_id):
        filters = [MySQLFilter.filter_equal(MySQLPracticeCentersTable.id_col, practice_center_id)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = MySQLPracticeCentersFilter().build_filters(form)

        orders = [MySQLPracticeCentersTable.name_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = ('INSERT INTO ' + MySQLPracticeCentersTable.table_name +
                     '(' + all_fields_to_add + ') VALUES (%s, %s, %s, %s)')

        return self.build_query(operation)
