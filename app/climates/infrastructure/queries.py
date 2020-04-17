from app.climates.infrastructure.tables import MySQLSportClimateTable, \
    MySQLPracticeCenterClimateTable, MySQLClimateTable
from app.interfaces.infrastructure.filters import MySQLFilter
from app.interfaces.infrastructure.queries import MySQLQuery


class MySQLClimateQuery(MySQLQuery):
    fake_name_col = 'name'

    def get_all_for_sport(self, sport_id):
        return self.get_all_for_type(sport_id,
                                     MySQLSportClimateTable.sport_id_col,
                                     MySQLSportClimateTable.climate_name_col,
                                     MySQLSportClimateTable.table_name)

    def get_all_for_practice_center(self, practice_center_id):
        return self.get_all_for_type(practice_center_id,
                                     MySQLPracticeCenterClimateTable.practice_center_id_col,
                                     MySQLPracticeCenterClimateTable.climate_name_col,
                                     MySQLPracticeCenterClimateTable.table_name)

    def get_all_for_type(self, type_id, type_id_col, climate_name_col, table_name):
        operation = (f'SELECT {climate_name_col} AS {self.fake_name_col}'
                     f' FROM {table_name}')

        filters = [MySQLFilter.filter_equal(type_id_col, type_id)]

        orders = [climate_name_col]

        return self.build_query(operation, filters, orders)

    def add(self):
        operation = (f'INSERT INTO {MySQLClimateTable.table_name}'
                     f' ({MySQLClimateTable.name_col})'
                     f' VALUES (%s)')

        return self.build_query(operation)

    def add_for_sport(self):
        return self.add_for_type(MySQLSportClimateTable.table_name,
                                 MySQLSportClimateTable.climate_name_col,
                                 MySQLSportClimateTable.sport_id_col)

    def add_for_practice_center(self):
        return self.add_for_type(MySQLPracticeCenterClimateTable.table_name,
                                 MySQLPracticeCenterClimateTable.climate_name_col,
                                 MySQLPracticeCenterClimateTable.practice_center_id_col)

    def add_for_type(self, table_name, climate_name_col, type_id_col):
        operation = (f'INSERT INTO {table_name}'
                     f' ({climate_name_col}'
                     f', {type_id_col})'
                     f' VALUES (%s, %s);')

        return self.build_query(operation)
