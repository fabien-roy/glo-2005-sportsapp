from app.repositories.mysql_filters import MySQLFilter
from app.repositories.mysql_tables import MySQLEquipmentsTable


class MySQLEquipmentsFilter(MySQLFilter):
    def get_col_names(self):
        return [MySQLEquipmentsTable.category_col,
                MySQLEquipmentsTable.name_col,
                MySQLEquipmentsTable.description_col]

    def get_values(self, form=None):
        return [] if form is None else [form.name.data, form.category.data, form.description.data]
