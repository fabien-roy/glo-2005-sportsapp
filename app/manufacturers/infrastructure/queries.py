from app.manufacturers.infrastructure.tables import MySQLManufacturerTable as Manufacturers
from app.interfaces.infrastructure.queries import MySQLQuery

all_fields_to_add = f'{Manufacturers.name_col}'


class MySQLManufacturerQuery(MySQLQuery):
    def add(self):
        operation = (f'INSERT INTO {Manufacturers.table_name}'
                     f'({all_fields_to_add}) VALUES (%s)')

        return self.build_query(operation)
