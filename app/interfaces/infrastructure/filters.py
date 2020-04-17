class MySQLFilter:
    @staticmethod
    def filter_equal(col, value):
        return f'{col} = {value}'

    @staticmethod
    def filter_equal_string(col, value):
        return f'{col} = \'{value}\''

    @staticmethod
    def filter_like(col, value):
        return f'{col} LIKE \'%{value}%\''

    def get_col_names(self):
        pass

    def get_values(self, form=None):
        pass

    def build_filters(self, form=None):
        if form is not None:
            if form.any_field.data != '':
                return self.build_general_filters(self.get_col_names(), form.any_field.data)

            return self.build_advanced_filters(self.get_col_names(), self.get_values(form))

        return [], True

    def build_general_filters(self, col_names, value):
        filters = []

        for col_name in col_names:
            filters.append(self.filter_like(col_name, value))

        return filters, False

    def build_advanced_filters(self, col_names, values):
        filters = []

        for i, value in enumerate(values):
            if value != '':
                filters.append(self.filter_like(col_names[i], value))

        return filters, True
