from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_queries import MySQLQuery
from app.repositories.mysql_tables import MySQLPracticeCentersTable


class MySQLPracticeCentersFilter(MySQLFilter):
    def build_filters(self, form=None):
        filters = []

        if form is not None:

            if form.all.data != '':
                return self.build_general_filters(form)
            else:
                if form.name.data != '':
                    filters.append(self.filter_like(MySQLPracticeCentersTable.name_col, form.name.data))

                if form.email.data != '':
                    filters.append(self.filter_like(MySQLPracticeCentersTable.email_col, form.email.data))

                if form.web_site.data != '':
                    filters.append(self.filter_like(MySQLPracticeCentersTable.web_site_col, form.web_site.data))

                if form.phone_number.data != '':
                    filters.append(self.filter_like(MySQLPracticeCentersTable.phone_number_col, form.phone_number.data))

        return filters, True

    def build_general_filters(self, form=None):
        filters = [self.filter_like(MySQLPracticeCentersTable.name_col, form.all.data),
                   self.filter_like(MySQLPracticeCentersTable.email_col, form.all.data),
                   self.filter_like(MySQLPracticeCentersTable.web_site_col, form.all.data),
                   self.filter_like(MySQLPracticeCentersTable.phone_number_col, form.all.data)]

        return filters, False
