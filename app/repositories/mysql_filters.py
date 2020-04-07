class MySQLFilter:
    @staticmethod
    def filter_equal(col, filter):
        return "{} = {}".format(col, filter)

    @staticmethod
    def filter_equal_string(col, filter):
        return "{} = '{}'".format(col, filter)

    @staticmethod
    def filter_like(col, filter):
        return "{} LIKE '%{}%'".format(col, filter)

    def build_general_filters(self, col_names, value):
        filters = []

        for col_name in col_names:
            filters.append(self.filter_like(col_name, value))

        return filters, False

    def build_advanced_filters(self, col_names, values):
        filters = []

        for i in range(0, len(col_names)):
            if values[i] != '':
                filters.append(self.filter_like(col_names[i], values[i]))

        return filters, True
