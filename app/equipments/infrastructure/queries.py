from app.equipments.infrastructure.filters import MySQLEquipmentFilter as Filter
from app.equipments.infrastructure.tables import MySQLEquipmentTable as Equipments
from app.interfaces.infrastructure.filters import MySQLFilter
from app.interfaces.infrastructure.queries import MySQLQuery

all_fields_to_add = (f'{Equipments.category_col}'
                     f', {Equipments.name_col}'
                     f', {Equipments.description_col}')

all_fields = f'{Equipments.id_col}, {all_fields_to_add}'

select_all_operation = f'SELECT {all_fields} FROM {Equipments.table_name}'


class MySQLEquipmentsQuery(MySQLQuery):
    def get(self, equipment_id):
        filters = [MySQLFilter.filter_equal(Equipments.id_col, equipment_id)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = Filter().build_filters(form)

        orders = [Equipments.name_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = (f'INSERT INTO {Equipments.table_name}'
                     f'({all_fields_to_add}) VALUES (%s, %s, %s)')

        return self.build_query(operation)
