from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLClimatesTable, MySQLSportClimatesTable, MySQLPracticeCenterClimatesTable


class MySQLClimatesQuery(MySQLQuery):
    def get_all_for_sport(self, sport_id):
        return self.get_all_for_type(sport_id,
                                     MySQLSportClimatesTable.sport_id_col,
                                     MySQLSportClimatesTable.climate_name_col,
                                     MySQLSportClimatesTable.table_name)

    def get_all_for_practice_center(self, practice_center_id):
        return self.get_all_for_type(practice_center_id,
                                     MySQLPracticeCenterClimatesTable.practice_center_id_col,
                                     MySQLPracticeCenterClimatesTable.climate_name_col,
                                     MySQLPracticeCenterClimatesTable.table_name)

    def get_all_for_type(self, type_id, type_id_col, climate_name_col, table_name):
        operation = ('SELECT ' + climate_name_col +
                     ' FROM ' + table_name)

        filters = [self.filter_equal(type_id_col, type_id)]

        orders = [climate_name_col]

        return self.build_query(operation, filters, orders)

    def add(self):
        operation = ('INSERT INTO ' + MySQLClimatesTable.table_name +
                     ' (' + MySQLClimatesTable.name_col + ')' +
                     ' VALUES (%s)')

        return self.build_query(operation)

    def add_for_sport(self):
        return self.add_for_type(MySQLSportClimatesTable.table_name,
                                 MySQLSportClimatesTable.climate_name_col,
                                 MySQLSportClimatesTable.sport_id_col)

    def add_for_practice_center(self):
        return self.add_for_type(MySQLPracticeCenterClimatesTable.table_name,
                                 MySQLPracticeCenterClimatesTable.climate_name_col,
                                 MySQLPracticeCenterClimatesTable.practice_center_id_col)

    def add_for_type(self, table_name, climate_name_col, type_id_col):
        operation = ('INSERT INTO ' + table_name +
                     ' (' + climate_name_col +
                     ', ' + type_id_col + ')' +
                     ' VALUES (%s, %s);')

        return self.build_query(operation)
