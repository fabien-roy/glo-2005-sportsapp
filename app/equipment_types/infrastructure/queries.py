from app.equipment_types.infrastructure.tables import MySQLEquipmentTypeTable as EquipmentTypes
from app.interfaces.infrastructure.queries import MySQLQuery

all_fields_to_add = f'{EquipmentTypes.name_col}'


class MySQLCategoryQuery(MySQLQuery):
    def add(self):
        operation = (f'INSERT INTO {EquipmentTypes.table_name}'
                     f'({all_fields_to_add}) VALUES (%s)')

        return self.build_query(operation)
