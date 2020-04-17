from app.interfaces.infrastructure.filters import MySQLFilter
from app.equipments.infrastructure.tables import MySQLEquipmentTable as Equipments


class MySQLEquipmentFilter(MySQLFilter):
    def get_col_names(self):
        return [Equipments.category_col,
                Equipments.name_col,
                Equipments.description_col]

    def get_values(self, form=None):
        return [] if form is None else [form.category.data, form.name.data, form.description.data]
