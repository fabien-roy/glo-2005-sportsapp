from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_tables import MySQLPracticeCentersTable

col_names = [MySQLPracticeCentersTable.name_col,
             MySQLPracticeCentersTable.email_col,
             MySQLPracticeCentersTable.web_site_col,
             MySQLPracticeCentersTable.phone_number_col]


class MySQLPracticeCentersFilter(MySQLFilter):
    def build_filters(self, form=None):
        if form is not None:
            if form.all.data != '':
                return super().build_general_filters(col_names, form.all.data)
            else:
                return super().build_advanced_filters(col_names,
                                                      [form.name.data,
                                                       form.email.data,
                                                       form.web_site.data,
                                                       form.phone_number.data])

        return [], True
