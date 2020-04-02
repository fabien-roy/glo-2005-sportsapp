from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLUsersTable


class MySQLUsersQuery(MySQLQuery):
    def get(self, username):
        operation = ('SELECT ' + MySQLUsersTable.username_col +
                     ', ' + MySQLUsersTable.email_col +
                     ', ' + MySQLUsersTable.first_name_col +
                     ', ' + MySQLUsersTable.last_name_col +
                     ', ' + MySQLUsersTable.phone_number_col +
                     ', ' + MySQLUsersTable.creation_date_col +
                     ', ' + MySQLUsersTable.last_login_date_col +
                     ' FROM ' + MySQLUsersTable.table_name)

        filters = [self.filter_equal_string(MySQLUsersTable.username_col, username)]

        return self.build_query(operation, filters)


    def get_all(self, form=None):
        operation = ('SELECT ' + MySQLUsersTable.username_col +
                     ', ' + MySQLUsersTable.email_col +
                     ', ' + MySQLUsersTable.first_name_col +
                     ', ' + MySQLUsersTable.last_name_col +
                     ', ' + MySQLUsersTable.phone_number_col +
                     ', ' + MySQLUsersTable.creation_date_col +
                     ', ' + MySQLUsersTable.last_login_date_col +
                     ' FROM ' + MySQLUsersTable.table_name)

        # TODO : Search form for users
        filters = []

        orders = [MySQLUsersTable.username_col]

        return self.build_query(operation, filters, orders)


    def add(self):
        operation = ('INSERT INTO ' + MySQLUsersTable.table_name +
                     ' (' + MySQLUsersTable.username_col +
                     ', ' + MySQLUsersTable.email_col +
                     ', ' + MySQLUsersTable.first_name_col +
                     ', ' + MySQLUsersTable.last_name_col +
                     ', ' + MySQLUsersTable.phone_number_col +
                     ', ' + MySQLUsersTable.creation_date_col + ')' +
                     ' VALUES (%s, %s, %s, %s, %s, %s)')

        return self.build_query(operation)
