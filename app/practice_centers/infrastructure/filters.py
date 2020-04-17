from app.interfaces.infrastructure.filters import MySQLFilter
from app.practice_centers.infrastructure.tables import MySQLPracticeCenterTable as PracticeCenters


class MySQLPracticeCenterFilter(MySQLFilter):
    def get_col_names(self):
        return [PracticeCenters.name_col,
                PracticeCenters.email_col,
                PracticeCenters.web_site_col,
                PracticeCenters.phone_number_col]

    def get_values(self, form=None):
        return [] if form is None else [form.name.data, form.email.data, form.web_site.data,
                                        form.phone_number.data]
