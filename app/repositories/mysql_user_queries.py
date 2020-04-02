from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLUsersTable
from app.repositories.mysql_user_filters import MySQLUsersFilter

all_fields_to_add = (MySQLUsersTable.username_col +
                     ", " + MySQLUsersTable.email_col +
                     ', ' + MySQLUsersTable.first_name_col +
                     ', ' + MySQLUsersTable.last_name_col +
                     ', ' + MySQLUsersTable.phone_number_col +
                     ', ' + MySQLUsersTable.creation_date_col)

all_fields = (all_fields_to_add + ', ' + MySQLUsersTable.last_login_date_col)

select_all_operation = ('SELECT ' + all_fields + ' FROM ' + MySQLUsersTable.table_name)


class MySQLUsersQuery(MySQLQuery):

    def get(self, username):
        filters = [self.filter_equal_string(MySQLUsersTable.username_col, username)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = MySQLUsersFilter().build_filters(form)

        orders = [MySQLUsersTable.username_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = ('INSERT INTO ' + MySQLUsersTable.table_name +
                     ' (' + all_fields_to_add + ')' +
                     ' VALUES (%s, %s, %s, %s, %s, %s)')

        return self.build_query(operation)
