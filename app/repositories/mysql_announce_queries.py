from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLAnnouncesTable

all_fields_to_add = (f'{MySQLAnnouncesTable.shop_id_col}'
                     f', {MySQLAnnouncesTable.equipment_id_col}'
                     f', {MySQLAnnouncesTable.state_col}'
                     f', {MySQLAnnouncesTable.price_col}'
                     f', {MySQLAnnouncesTable.date_col}')

all_fields = f'{MySQLAnnouncesTable.id_col}, {all_fields_to_add}'

select_all_operation = f'SELECT {all_fields} FROM {MySQLAnnouncesTable.table_name}'


class MySQLAnnouncesQuery(MySQLQuery):
    def get_all_for_shop(self, shop_id):
        filters = [MySQLFilter.filter_equal(MySQLAnnouncesTable.shop_id_col, shop_id)]

        return self.build_query(select_all_operation, filters)

    def get_all_for_equipment(self, equipment_id):
        filters = [MySQLFilter.filter_equal(MySQLAnnouncesTable.equipment_id_col, equipment_id)]

        return self.build_query(select_all_operation, filters)

    def add(self):
        operation = (f'INSERT INTO {MySQLAnnouncesTable.table_name}'
                     f'({all_fields_to_add}) VALUES (%s, %s, %s, %s, %s)')

        return self.build_query(operation)
