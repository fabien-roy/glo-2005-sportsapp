from app.interfaces.infrastructure.filters import MySQLFilter
from app.sports.infrastructure.tables import MySQLSportTable as Sports
from app.climates.infrastructure.tables import MySQLSportClimateTable as SportClimates


class MySQLSportFilter(MySQLFilter):
    joined_climate_name_col = f'C.{SportClimates.climate_name_col}'

    def get_col_names(self):
        return [self.joined_climate_name_col, Sports.name_col]

    def get_values(self, form=None):
        return [] if form is None else [form.climate.data, form.name.data]
