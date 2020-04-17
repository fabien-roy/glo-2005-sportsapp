from app.announces.infrastructure.tables import MySQLAnnounceTable as Announces
from app.equipments.infrastructure.tables import MySQLEquipmentTable as Equipments
from app.interfaces.infrastructure.filters import MySQLFilter
from app.interfaces.infrastructure.queries import MySQLQuery
from app.interfaces.infrastructure.tables import \
    MySQLShopsTable as Shops

all_fields_to_add = (f'{Announces.shop_id_col}'
                     f', {Announces.equipment_id_col}'
                     f', {Announces.state_col}'
                     f', {Announces.price_col}'
                     f', {Announces.date_col}')


class MySQLAnnounceQuery(MySQLQuery):
    fake_shop_name_col = 'shop_name'
    fake_equipment_name_col = 'equipment_name'

    def get_all_for_shop(self, shop_id):
        filters = [MySQLFilter.filter_equal(Announces.shop_id_col, shop_id)]

        return self.get_all(filters)

    def get_all_for_equipment(self, equipment_id):
        filters = [MySQLFilter.filter_equal(Announces.equipment_id_col, equipment_id)]

        return self.get_all(filters)

    def get_all(self, filters):
        operation = (f'SELECT A.{Announces.id_col}'
                     f', {all_fields_to_add}'
                     f', S.{Shops.name_col} AS {self.fake_shop_name_col}'
                     f', E.{Equipments.name_col} AS {self.fake_equipment_name_col}'
                     f' FROM {Announces.table_name} AS A'
                     f' JOIN {Shops.table_name} S ON S.{Shops.id_col} ='
                     f' A.{Announces.shop_id_col}'
                     f' JOIN {Equipments.table_name} E ON E.{Equipments.id_col} ='
                     f' A.{Announces.equipment_id_col}')

        return self.build_query(operation, filters)

    def add(self):
        operation = (f'INSERT INTO {Announces.table_name}'
                     f'({all_fields_to_add}) VALUES (%s, %s, %s, %s, %s)')

        return self.build_query(operation)
