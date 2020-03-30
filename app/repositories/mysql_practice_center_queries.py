from app.repositories.mysql_queries import build_query, filter_like, filter_equal


class MySQLPracticeCentersQuery:
    table_name = 'practice_centers'

    id_col = 'id'
    name_col = 'name'
    email_col = 'email'
    web_site_col = 'web_site'
    phone_number_col = 'phone_number'

    def get_all(self, form=None):
        operation = ('SELECT ' + self.id_col + ', ' + self.name_col + ', ' + self.email_col + ', ' +
                     self.web_site_col + ', ' + self.phone_number_col +
                     ' FROM ' + self.table_name)

        if form is None:
            filters = None
        else:
            filters = []

        orders = [self.name_col]

        return build_query(operation, filters, orders)

    def get(self, practice_center_id):
        operation = ('SELECT ' + self.id_col + ', ' + self.name_col + ', ' + self.email_col + ', ' +
                     self.web_site_col + ', ' + self.phone_number_col +
                     ' FROM ' + self.table_name)

        filters = [filter_equal(self.id_col, practice_center_id)]

        return build_query(operation, filters)

    def add(self):
        operation = ('INSERT INTO ' + self.table_name +
                     ' (' + self.name_col + ', ' + self.email_col + ', ' + self.web_site_col +
                     ', ' + self.phone_number_col + ')' +
                     ' VALUES (%s, %s, %s, %s);')

        return build_query(operation)
