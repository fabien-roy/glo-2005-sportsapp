from app.interfaces.infrastructure.filters import MySQLFilter
from app.interfaces.infrastructure.queries import MySQLQuery
from app.users.infrastructure.filters import MySQLUserFilter as Filter
from app.users.infrastructure.tables import MySQLUserTable as Users

all_fields_to_add = (f'{Users.username_col}'
                     f', {Users.email_col}'
                     f', {Users.first_name_col}'
                     f', {Users.last_name_col}'
                     f', {Users.phone_number_col}'
                     f', {Users.creation_date_col}')

all_fields = f'{all_fields_to_add}, {Users.last_login_date_col}'

select_all_operation = f'SELECT {all_fields} FROM {Users.table_name}'


class MySQLUserQuery(MySQLQuery):
    def get(self, username):
        filters = [MySQLFilter.filter_equal_string(Users.username_col, username)]

        return self.build_query(select_all_operation, filters)

    def get_all(self, form=None):
        filters, inner_filtering = Filter().build_filters(form)

        orders = [Users.username_col]

        return self.build_query(select_all_operation, filters, orders, inner_filtering)

    def add(self):
        operation = (f'INSERT INTO {Users.table_name}'
                     f' ({all_fields_to_add})'
                     f' VALUES (%s, %s, %s, %s, %s, %s)')

        return self.build_query(operation)
