from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLSportsTable


class MySQLSportsQuery(MySQLQuery):
    def get_all(self, form=None):
        operation = ('SELECT ' + MySQLSportsTable.id_col +
                     ', ' + MySQLSportsTable.name_col +
                     ' FROM ' + MySQLSportsTable.table_name)

        if form is None:
            filters = None
        else:
            filters = []

            if form.name is not None:
                filters.append(self.filter_like(MySQLSportsTable.name_col, form.name.data))

        orders = [MySQLSportsTable.name_col]

        return self.build_query(operation, filters, orders)

    def get(self, sport_id):
        operation = ('SELECT ' + MySQLSportsTable.id_col +
                     ', ' + MySQLSportsTable.name_col +
                     ' FROM ' + MySQLSportsTable.table_name)

        filters = [self.filter_equal(MySQLSportsTable.id_col, sport_id)]

        return self.build_query(operation, filters)

    def add(self):
        operation = ('INSERT INTO ' + MySQLSportsTable.table_name +
                     ' (' + MySQLSportsTable.name_col + ')' +
                     ' VALUES (%s)')

        return self.build_query(operation)
