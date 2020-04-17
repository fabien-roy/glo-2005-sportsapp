from app.interfaces.infrastructure.filters import MySQLFilter
from app.users.infrastructure.tables import MySQLUserTable as Users


class MySQLUserFilter(MySQLFilter):
    def get_col_names(self):
        return [Users.username_col,
                Users.email_col,
                Users.first_name_col,
                Users.last_name_col,
                Users.phone_number_col]

    def get_values(self, form=None):
        return [] if form is None else [form.username.data, form.email.data, form.first_name.data,
                                        form.last_name.data, form.phone_number.data]
