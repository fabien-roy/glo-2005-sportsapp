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
