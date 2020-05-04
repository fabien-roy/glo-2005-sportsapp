from app.interfaces.infrastructure.filters import MySQLFilter
from app.interfaces.infrastructure.queries import MySQLQuery
from app.equipment_types.infrastructure.tables import MySQLSportEquipmentTypeTable as \
    SportEquipmentTypes
from app.sports.infrastructure.filters import MySQLSportFilter as Filter
from app.sports.infrastructure.tables import MySQLSportTable as Sports

all_fields_to_add = Sports.name_col


class MySQLSportQuery(MySQLQuery):
    fake_average_note_col = 'average_note'
    get_average_note = 'get_sport_average_note'

    select_all_operation = (f'SELECT {Sports.id_col},'
                            f'{all_fields_to_add},'
                            f'{get_average_note}({Sports.id_col}) AS {fake_average_note_col}'
                            f' FROM {Sports.table_name}')

    def get(self, sport_id):
        filters = [MySQLFilter.filter_equal(Sports.id_col, sport_id)]

        return self.build_query(self.select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = Filter().build_filters(form)

        orders = [self.fake_average_note_col]

        return self.build_query(self.select_all_operation, filters, orders, inner_filtering, True)

    def get_all_for_equipment_type(self, type_id):
        operation = (f'SELECT S.{Sports.id_col}, S.{Sports.name_col} '
                     f'FROM {Sports.table_name} S '
                     f'JOIN {SportEquipmentTypes.table_name} E ON '
                     f'E.{SportEquipmentTypes.sport_id_col} = S.{Sports.id_col}')

        filters = [MySQLFilter.filter_equal(SportEquipmentTypes.type_id_col, type_id)]

        orders = [f'S.{Sports.name_col}']

        return self.build_query(operation, filters, orders)

    def add(self):
        operation = (f'INSERT INTO {Sports.table_name}'
                     f' ({all_fields_to_add})'
                     f' VALUES (%s)')

        return self.build_query(operation)
