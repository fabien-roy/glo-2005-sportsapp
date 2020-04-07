from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_tables import MySQLUsersTable

col_names = [MySQLUsersTable.username_col,
             MySQLUsersTable.email_col,
             MySQLUsersTable.first_name_col,
             MySQLUsersTable.last_name_col,
             MySQLUsersTable.phone_number_col]


class MySQLUsersFilter(MySQLFilter):
    def build_filters(self, form=None):
        if form is not None:
            if form.all.data != '':
                return super().build_general_filters(col_names, form.all.data)
            else:
                return super().build_advanced_filters(col_names,
                                                      [form.username.data,
                                                       form.email.data,
                                                       form.first_name.data,
                                                       form.last_name.data,
                                                       form.phone_number.data])
        else:
            return [], True

