from app.interfaces.infrastructure.filters import MySQLFilter
from app.interfaces.infrastructure.queries import MySQLQuery
from app.equipment_types.infrastructure.tables import MySQLSportEquipmentTypeTable as \
    SportEquipmentTypes
from app.sports.infrastructure.filters import MySQLSportFilter as Filter
from app.sports.infrastructure.tables import MySQLSportTable as Sports
from app.climates.infrastructure.tables import MySQLSportClimateTable as SportClimates

select_all_simple_operation = (f'SELECT {Sports.id_col},'
                               f' {Sports.name_col}'
                               f' FROM {Sports.table_name}')


class MySQLSportQuery(MySQLQuery):
    fake_average_note_col = 'average_note'
    fake_count_col = 'count'
    get_average_note = 'get_sport_average_note'

    from_tables = (f" FROM {Sports.table_name} S"
                   f" LEFT JOIN {SportClimates.table_name} C ON C.{SportClimates.sport_id_col}"
                   f" = S.{Sports.id_col}")

    select_all_operation = (f'SELECT DISTINCT S.{Sports.id_col},'
                            f' S.{Sports.name_col},'
                            f' {get_average_note}({Sports.id_col}) AS {fake_average_note_col}'
                            f' {from_tables} ')

    select_count_operation = (f'SELECT COUNT(DISTINCT S.{Sports.id_col}) '
                              f' AS {fake_count_col} {from_tables}')

    def get_all(self, form=None, offset=None, per_page=None):
        filters, inner_filtering = Filter().build_filters(form)

        orders = [self.fake_average_note_col]

        return self.build_query(self.select_all_operation, filters, orders, inner_filtering, True,
                                offset, per_page)

    def get_count(self, form):
        filters, inner_filtering = Filter().build_filters(form)

        return self.build_query(self.select_count_operation, filters, None, inner_filtering)

    def get_all_for_equipment_type(self, type_id):
        operation = (f'SELECT S.{Sports.id_col}, S.{Sports.name_col} '
                     f'FROM {Sports.table_name} S '
                     f'JOIN {SportEquipmentTypes.table_name} E ON '
                     f'E.{SportEquipmentTypes.sport_id_col} = S.{Sports.id_col}')

        filters = [MySQLFilter.filter_equal(SportEquipmentTypes.type_id_col, type_id)]

        orders = [f'S.{Sports.name_col}']

        return self.build_query(operation, filters, orders)

    def get(self, sport_id):
        filters = [MySQLFilter.filter_equal(f'S.{Sports.id_col}', sport_id)]

        return self.build_query(self.select_all_operation, filters)

    def get_by_name(self, name):
        filters = [MySQLFilter.filter_equal_string(Sports.name_col, name)]

        return self.build_query(select_all_simple_operation, filters)

    def add(self):
        operation = f'INSERT INTO {Sports.table_name} ({Sports.name_col}) VALUES (%s)'

        return self.build_query(operation)
