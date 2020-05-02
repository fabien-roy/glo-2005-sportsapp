from app.interfaces.infrastructure.filters import MySQLFilter
from app.equipments.infrastructure.tables import MySQLEquipmentTable as Equipments
from app.manufacturers.infrastructure.tables import MySQLManufacturerTable as Manufacturers
from app.equipment_types.infrastructure.tables import MySQLEquipmentTypeTable as EquipmentTypes


class MySQLEquipmentFilter(MySQLFilter):
    joined_manufacturer_name_col = f'M.{Manufacturers.name_col}'
    joined_type_name_col = f'T.{EquipmentTypes.name_col}'

    def get_col_names(self):
        return [self.joined_manufacturer_name_col,
                self.joined_type_name_col,
                f'E.{Equipments.name_col}',
                f'E.{Equipments.description_col}']

    def get_values(self, form=None):
        return [] if form is None else [form.manufacturer.data, form.equipment_type.data,
                                        form.name.data, form.description.data]
