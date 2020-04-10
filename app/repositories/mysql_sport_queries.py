from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_sport_filters import MySQLSportsFilter
from app.repositories.mysql_tables import MySQLSportsTable

all_fields_to_add = MySQLSportsTable.name_col

all_fields = (MySQLSportsTable.id_col + ', ' + all_fields_to_add)

select_all_operation = ('SELECT ' + all_fields + ' FROM ' + MySQLSportsTable.table_name)


class MySQLSportsQuery(MySQLQuery):
    def get(self, sport_id):
        filters = [MySQLFilter.filter_equal(MySQLSportsTable.id_col, sport_id)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = MySQLSportsFilter().build_filters(form)

        orders = [MySQLSportsTable.name_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = ('INSERT INTO ' + MySQLSportsTable.table_name +
                     ' (' + all_fields_to_add + ')' +
                     ' VALUES (%s)')

        return self.build_query(operation)
