from app.repositories.mysql_queries import build_query, filter_like, filter_equal


class MySQLSportsQuery:
    table_name = 'sports'

    id_col = 'id'
    name_col = 'name'

    def get_all(self, form=None):
        operation = ('SELECT ' + self.id_col + ', ' + self.name_col +
                     ' FROM ' + self.table_name)

        if form is None:
            filters = None
        else:
            filters = []

            if form.name is not None:
                filters.append(filter_like(self.name_col, form.name.data))

        orders = [self.name_col]

        return build_query(operation, filters, orders)

    def get(self, sport_id):
        operation = ('SELECT ' + self.id_col + ', ' + self.name_col +
                     ' FROM ' + self.table_name)

        filters = [filter_equal(self.id_col, sport_id)]

        return build_query(operation, filters)

    def add(self):
        operation = ('INSERT INTO ' + self.table_name +
                     ' (' + self.name_col + ')' +
                     ' VALUES (%s);')

        return build_query(operation)
