from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_tables import MySQLShopsTable


class MySQLShopsFilter(MySQLFilter):
    def get_col_names(self):
        return [MySQLShopsTable.name_col,
                MySQLShopsTable.email_col,
                MySQLShopsTable.web_site_col,
                MySQLShopsTable.phone_number_col]

    def get_values(self, form=None):
        return [] if form is None else [form.name.data, form.email.data, form.web_site.data,
                                        form.phone_number.data]
