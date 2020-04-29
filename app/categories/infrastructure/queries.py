from app.categories.infrastructure.tables import MySQLCategoryTable as Categories
from app.interfaces.infrastructure.queries import MySQLQuery

all_fields_to_add = f'{Categories.name_col}'


class MySQLCategoryQuery(MySQLQuery):
    def add(self):
        operation = (f'INSERT INTO {Categories.table_name}'
                     f'({all_fields_to_add}) VALUES (%s)')

        return self.build_query(operation)
