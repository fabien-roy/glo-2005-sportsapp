def filter_equal(col, filter):
    return "{} = {}".format(col, filter)


def filter_like(col, filter):
    return '{} LIKE \'%{}%\''.format(col, filter)


def build_query(operation, filters=None, orders=None, inner_filtering=True):
    query = operation

    if filters is not None:
        query += ' WHERE {}'.format(filters[0])

        conjunction = 'AND' if inner_filtering else 'OR'

        for i in range(1, len(filters) - 1):
            query += ' {} {}'.format(conjunction, filters[i])

    if orders is not None:
        query += ' ORDER BY '

        for order in orders:
            query += order + ' '

    return '{};'.format(query)
