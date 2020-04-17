from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_tables import MySQLPracticeCentersTable


class MySQLPracticeCentersFilter(MySQLFilter):
    def get_col_names(self):
        return [MySQLPracticeCentersTable.name_col,
                MySQLPracticeCentersTable.email_col,
                MySQLPracticeCentersTable.web_site_col,
                MySQLPracticeCentersTable.phone_number_col]

    def get_values(self, form=None):
        return [] if form is None else [form.name.data, form.email.data, form.web_site.data,
                                        form.phone_number.data]
