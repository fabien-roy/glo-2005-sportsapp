from app.interfaces.infrastructure.filters import MySQLFilter
from app.interfaces.infrastructure.queries import MySQLQuery
from app.practice_centers.infrastructure.filters import MySQLPracticeCenterFilter as Filter
from app.practice_centers.infrastructure.tables import MySQLPracticeCenterTable as PracticeCenters
from app.climates.infrastructure.tables import MySQLPracticeCenterClimateTable as \
    PracticeCenterClimates

all_fields_to_add = (f'{PracticeCenters.name_col}'
                     f', {PracticeCenters.email_col}'
                     f', {PracticeCenters.web_site_col}'
                     f', {PracticeCenters.phone_number_col}')

all_fields = f'{PracticeCenters.id_col}, {all_fields_to_add}'

all_fields_with_alias = (f'P.{PracticeCenters.id_col}'
                         f', P.{PracticeCenters.name_col}'
                         f', P.{PracticeCenters.email_col}'
                         f', P.{PracticeCenters.web_site_col}'
                         f', P.{PracticeCenters.phone_number_col}')

select_all_simple_operation = f'SELECT {all_fields}, FROM {PracticeCenters.table_name}'


class MySQLPracticeCenterQuery(MySQLQuery):
    fake_count_col = 'count'
    fake_average_note_col = 'average_note'
    get_average_note = 'get_practice_center_average_note'

    from_tables = (f' FROM {PracticeCenters.table_name} P'
                   f' JOIN {PracticeCenterClimates.table_name} C ON '
                   f' C.{PracticeCenterClimates.practice_center_id_col} = '
                   f' P.{PracticeCenters.id_col}')

    select_all_operation = (f'SELECT {all_fields_with_alias},'
                            f' {get_average_note}({PracticeCenters.id_col})'
                            f' AS {fake_average_note_col}'
                            f' {from_tables}')

    select_count_operation = f'SELECT COUNT(*) AS {fake_count_col} {from_tables}'

    def get_all(self, form=None, offset=None, per_page=None):
        filters, inner_filtering = Filter().build_filters(form)

        orders = [self.fake_average_note_col]

        return self.build_query(self.select_all_operation, filters, orders, inner_filtering, True,
                                offset, per_page)

    def get_count(self, form):
        filters, inner_filtering = Filter().build_filters(form)

        return self.build_query(self.select_count_operation, filters, None, inner_filtering)

    def get(self, practice_center_id):
        filters = [MySQLFilter.filter_equal(PracticeCenters.id_col, practice_center_id)]

        return self.build_query(self.select_all_operation, filters)

    def get_by_name(self, name):
        filters = [MySQLFilter.filter_equal_string(PracticeCenters.name_col, name)]

        return self.build_query(select_all_simple_operation, filters)

    def add(self):
        operation = (f'INSERT INTO {PracticeCenters.table_name}'
                     f'({all_fields_to_add}) VALUES (%s, %s, %s, %s)')

        return self.build_query(operation)
