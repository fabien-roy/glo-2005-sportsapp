from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_tables import MySQLUsersTable


class MySQLUsersFilter(MySQLFilter):
    def get_col_names(self):
        return [MySQLUsersTable.username_col,
                MySQLUsersTable.email_col,
                MySQLUsersTable.first_name_col,
                MySQLUsersTable.last_name_col,
                MySQLUsersTable.phone_number_col]

    def get_values(self, form=None):
        return [] if form is None else [form.username.data, form.email.data, form.first_name.data,
                                        form.last_name.data, form.phone_number.data]
