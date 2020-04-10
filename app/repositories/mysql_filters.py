class MySQLFilter:
    @staticmethod
    def filter_equal(col, value):
        return "{} = {}".format(col, value)

    @staticmethod
    def filter_equal_string(col, value):
        return "{} = '{}'".format(col, value)

    @staticmethod
    def filter_like(col, value):
        return "{} LIKE '%{}%'".format(col, value)

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
