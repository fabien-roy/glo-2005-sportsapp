from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLUsersTable
from app.repositories.mysql_user_filters import MySQLUsersFilter

all_fields_to_add = (f'{MySQLUsersTable.username_col}'
                     f', {MySQLUsersTable.email_col}'
                     f', {MySQLUsersTable.first_name_col}'
                     f', {MySQLUsersTable.last_name_col}'
                     f', {MySQLUsersTable.phone_number_col}'
                     f', {MySQLUsersTable.creation_date_col}')

all_fields = f'{all_fields_to_add}, {MySQLUsersTable.last_login_date_col}'

select_all_operation = f'SELECT {all_fields} FROM {MySQLUsersTable.table_name}'


class MySQLUsersQuery(MySQLQuery):
    def get(self, username):
        filters = [MySQLFilter.filter_equal_string(MySQLUsersTable.username_col, username)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = MySQLUsersFilter().build_filters(form)

        orders = [MySQLUsersTable.username_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = (f'INSERT INTO {MySQLUsersTable.table_name}'
                     f' ({all_fields_to_add})'
                     f' VALUES (%s, %s, %s, %s, %s, %s)')

        return self.build_query(operation)
