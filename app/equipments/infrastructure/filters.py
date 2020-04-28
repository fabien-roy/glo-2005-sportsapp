from app.interfaces.infrastructure.filters import MySQLFilter
from app.equipments.infrastructure.tables import MySQLEquipmentTable as Equipments
from app.manufacturers.infrastructure.tables import MySQLManufacturerTable as Manufacturers


class MySQLEquipmentFilter(MySQLFilter):
    joined_manufacturer_name_col = f'M.{Manufacturers.name_col}'

    def get_col_names(self):
        return [self.joined_manufacturer_name_col,
                f'E.{Equipments.category_col}',
                f'E.{Equipments.name_col}',
                f'E.{Equipments.description_col}']

    def get_values(self, form=None):
        return [] if form is None else [form.manufacturer_name.data, form.category.data,
                                        form.name.data, form.description.data]
