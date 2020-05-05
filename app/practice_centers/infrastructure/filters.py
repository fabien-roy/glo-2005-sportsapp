from app.interfaces.infrastructure.filters import MySQLFilter
from app.practice_centers.infrastructure.tables import MySQLPracticeCenterTable as PracticeCenters
from app.climates.infrastructure.tables import MySQLPracticeCenterClimateTable as \
    PracticeCenterClimates


class MySQLPracticeCenterFilter(MySQLFilter):
    joined_climate_name_col = f'C.{PracticeCenterClimates.climate_name_col}'

    def get_col_names(self):
        return [self.joined_climate_name_col,
                PracticeCenters.name_col,
                PracticeCenters.email_col,
                PracticeCenters.web_site_col,
                PracticeCenters.phone_number_col]

    def get_values(self, form=None):
        return [] if form is None else [form.climate.data, form.name.data, form.email.data,
                                        form.web_site.data, form.phone_number.data]
