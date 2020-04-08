from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_tables import MySQLShopsTable

col_names = [MySQLShopsTable.name_col,
             MySQLShopsTable.email_col,
             MySQLShopsTable.web_site_col,
             MySQLShopsTable.phone_number_col]


class MySQLShopsFilter(MySQLFilter):
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
