from app.interfaces.infrastructure.filters import MySQLFilter
from app.sports.infrastructure.tables import MySQLSportTable as Sports


class MySQLSportFilter(MySQLFilter):
    def get_col_names(self):
        return [Sports.name_col]

    def get_values(self, form=None):
        return [] if form is None else [form.name.data]
