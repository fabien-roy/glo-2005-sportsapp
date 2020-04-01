from app.repositories.mysql_queries import build_query, filter_equal, filter_equal_string


class MySQLUsersQuery:
    table_name = 'users'

    username_col = 'username'
    email_col = 'email'
    first_name_col = 'first_name'
    last_name_col = 'last_name'
    phone_number_col = 'phone_number'
    creation_date_col = 'creation_date'
    last_login_date_col = 'last_login_date'

    def get_all(self, form=None):
        operation = ('SELECT ' + self.username_col + ', ' + self.email_col + ', ' + self.first_name_col + ', ' +
                     self.last_name_col + ', ' + self.phone_number_col + ', ' + self.creation_date_col + ', ' +
                     self.last_login_date_col +
                     ' FROM ' + self.table_name)

        # TODO : Search form for users
        filters = []

        orders = [self.username_col]

        return build_query(operation, filters, orders)

    def get(self, username):
        operation = ('SELECT ' + self.username_col + ', ' + self.email_col + ', ' + self.first_name_col + ', ' +
                     self.last_name_col + ', ' + self.phone_number_col + ', ' + self.creation_date_col + ', ' +
                     self.last_login_date_col +
                     ' FROM ' + self.table_name)

        filters = [filter_equal_string(self.username_col, username)]

        return build_query(operation, filters)

    def add(self):
        operation = ('INSERT INTO ' + self.table_name +
                     ' (' + self.username_col + ', ' + self.email_col + ', ' + self.first_name_col + ', ' +
                     self.last_name_col + ', ' + self.phone_number_col + ', ' + self.creation_date_col + ')' +
                     ' VALUES (%s, %s, %s, %s, %s, %s)')

        return build_query(operation)
