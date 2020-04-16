from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_equipment_filters import MySQLEquipmentsFilter
from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLEquipmentsTable

all_fields_to_add = (f'{MySQLEquipmentsTable.name_col}'
                     f', {MySQLEquipmentsTable.category_col}'
                     f', {MySQLEquipmentsTable.description_col}')

all_fields = f'{MySQLEquipmentsTable.id_col}, {all_fields_to_add}'

select_all_operation = f'SELECT {all_fields} FROM {MySQLEquipmentsTable.table_name}'


class MySQLEquipmentsQuery(MySQLQuery):
    def get(self, equipment_id):
        filters = [MySQLFilter.filter_equal(MySQLEquipmentsTable.id_col, equipment_id)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = MySQLEquipmentsFilter().build_filters(form)

        orders = [MySQLEquipmentsTable.name_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = (f'INSERT INTO {MySQLEquipmentsTable.table_name}'
                     f'({all_fields_to_add}) VALUES (%s, %s, %s)')

        return self.build_query(operation)
