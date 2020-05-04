from app.admin.infrastructure.tables import MySQLStatEventsTable as StatEvents
from app.interfaces.infrastructure.queries import MySQLQuery

all_fields = f'{StatEvents.type_name_col}, {StatEvents.date_col}'

select_all_operation = f'SELECT {all_fields} FROM {StatEvents.table_name}'


class MySQLStatEventQuery(MySQLQuery):

    def get_all(self):
        orders = [StatEvents.type_name_col]

        return self.build_query(select_all_operation, None, orders)

    def add(self):
        operation = f'INSERT INTO {StatEvents.table_name} ({all_fields}) VALUES (%s, %s)'

        return self.build_query(operation)
