from app.interfaces.infrastructure.filters import MySQLFilter
from app.interfaces.infrastructure.queries import MySQLQuery
from app.sports.infrastructure.filters import MySQLSportFilter as Filter
from app.sports.infrastructure.tables import MySQLSportTable as Sports

all_fields_to_add = Sports.name_col

all_fields = f'{Sports.id_col}, {all_fields_to_add}'

select_all_operation = f'SELECT {all_fields} FROM {Sports.table_name}'


class MySQLSportQuery(MySQLQuery):
    def get(self, sport_id):
        filters = [MySQLFilter.filter_equal(Sports.id_col, sport_id)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = Filter().build_filters(form)

        orders = [Sports.name_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = (f'INSERT INTO {Sports.table_name}'
                     f' ({all_fields_to_add})'
                     f' VALUES (%s)')

        return self.build_query(operation)
