from app.interfaces.infrastructure.filters import MySQLFilter
from app.manufacturers.infrastructure.tables import MySQLManufacturerTable as Manufacturers
from app.interfaces.infrastructure.queries import MySQLQuery

all_fields_to_add = f'{Manufacturers.name_col}'

all_fields = f'{Manufacturers.id_col}, {all_fields_to_add}'

select_all_operation = f'SELECT {all_fields} FROM {Manufacturers.table_name}'


class MySQLManufacturerQuery(MySQLQuery):
    def add(self):
        operation = (f'INSERT INTO {Manufacturers.table_name}'
                     f'({all_fields_to_add}) VALUES (%s)')

        return self.build_query(operation)

    def get_by_name(self, name):
        filters = [MySQLFilter.filter_equal_string(f'{Manufacturers.name_col}', name)]

        return self.build_query(select_all_operation, filters)
