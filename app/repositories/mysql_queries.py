class MySQLQuery:
    @staticmethod
    def build_query(operation, filters=None, orders=None, inner_filtering=True):
        query = operation

        if filters is not None and len(filters) > 0:
            query += ' WHERE {}'.format(filters[0])

            conjunction = 'AND' if inner_filtering else 'OR'

            for i in range(1, len(filters)):
                query += ' {} {}'.format(conjunction, filters[i])

        if orders is not None and len(orders) > 0:
            query += ' ORDER BY '

            for order in orders:
                query += order + ' '

        return '{};'.format(query)
