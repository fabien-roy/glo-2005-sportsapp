from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLClimatesTable, MySQLSportClimatesTable


class MySQLClimatesQuery(MySQLQuery):
    def get_all_for_sport(self, sport_id):
        operation = ('SELECT ' + MySQLSportClimatesTable.climate_name_col +
                     ' FROM ' + MySQLSportClimatesTable.table_name)

        filters = [self.filter_equal(MySQLSportClimatesTable.sport_id_col, sport_id)]

        orders = [MySQLSportClimatesTable.climate_name_col]

        return self.build_query(operation, filters, orders)

    def add(self):
        operation = ('INSERT INTO ' + MySQLClimatesTable.table_name +
                     ' (' + MySQLClimatesTable.name_col + ')' +
                     ' VALUES (%s)')

        return self.build_query(operation)

    def add_for_sport(self):
        operation = ('INSERT INTO ' + MySQLSportClimatesTable.table_name +
                     ' (' + MySQLSportClimatesTable.sport_id_col +
                     ', ' + MySQLSportClimatesTable.climate_name_col + ')' +
                     ' VALUES (%s, %s);')

        return self.build_query(operation)
