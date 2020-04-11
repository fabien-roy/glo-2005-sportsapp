from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_equipment_filters import MySQLEquipmentsFilter
from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLEquipmentsTable

all_fields_to_add = (MySQLEquipmentsTable.name_col +
                     ', ' + MySQLEquipmentsTable.category_col +
                     ', ' + MySQLEquipmentsTable.description_col)

all_fields = (MySQLEquipmentsTable.id_col + ', ' + all_fields_to_add)

select_all_operation = ('SELECT ' + all_fields + ' FROM ' + MySQLEquipmentsTable.table_name)


class MySQLEquipmentsQuery(MySQLQuery):
    def get(self, equipment_id):
        filters = [MySQLFilter.filter_equal(MySQLEquipmentsTable.id_col, equipment_id)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = MySQLEquipmentsFilter().build_filters(form)

        orders = [MySQLEquipmentsTable.name_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = ('INSERT INTO ' + MySQLEquipmentsTable.table_name +
                     '(' + all_fields_to_add + ') VALUES (%s, %s, %s, %s)')

        return self.build_query(operation)
