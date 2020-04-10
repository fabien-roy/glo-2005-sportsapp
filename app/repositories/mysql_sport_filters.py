from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_tables import MySQLSportsTable

col_names = [MySQLSportsTable.name_col]


class MySQLSportsFilter(MySQLFilter):
    def build_filters(self, form=None):
        if form is not None:
            if form.all.data != '':
                return super().build_general_filters(col_names, form.all.data)
            else:
                return super().build_advanced_filters(col_names, [form.name.data])
        else:
            return [], True

