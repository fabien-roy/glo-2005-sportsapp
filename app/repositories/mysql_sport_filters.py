from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_tables import MySQLSportsTable


class MySQLSportsFilter(MySQLFilter):
    def get_col_names(self):
        return [MySQLSportsTable.name_col]

    def get_values(self, form=None):
        return [] if form is None else [form.name.data]
