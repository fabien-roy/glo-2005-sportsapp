from app.equipments.infrastructure.filters import MySQLEquipmentFilter as Filter
from app.equipments.infrastructure.tables import MySQLEquipmentTable as Equipments
from app.interfaces.infrastructure.filters import MySQLFilter
from app.interfaces.infrastructure.queries import MySQLQuery
from app.manufacturers.infrastructure.tables import MySQLManufacturerTable as Manufacturers

all_fields_to_add = (f'{Equipments.manufacturer_id_col}'
                     f', {Equipments.category_col}'
                     f', {Equipments.name_col}'
                     f', {Equipments.description_col}')


class MySQLEquipmentQuery(MySQLQuery):
    fake_manufacturer_name_col = 'manufacturer_name'

    select_all_operation = (f'SELECT E.{Equipments.id_col}'
                            f', {Filter.joined_manufacturer_name_col} AS'
                            f' {fake_manufacturer_name_col}'
                            f', E.{Equipments.category_col}'
                            f', E.{Equipments.name_col}'
                            f', E.{Equipments.description_col}'
                            f' FROM {Equipments.table_name} E'
                            f' JOIN {Manufacturers.table_name} M ON M.{Manufacturers.id_col} ='
                            f' E.{Equipments.manufacturer_id_col}')

    def get(self, equipment_id):
        filters = [MySQLFilter.filter_equal(f'E.{Equipments.id_col}', equipment_id)]

        return self.build_query(self.select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = Filter().build_filters(form)

        orders = [f'E.{Equipments.name_col}']

        return self.build_query(self.select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = (f'INSERT INTO {Equipments.table_name}'
                     f'({all_fields_to_add}) VALUES (%s, %s, %s, %s)')

        return self.build_query(operation)
