def filter_equal(col, filter):
    return "{} = {}".format(col, filter)


def filter_like(col, filter):
    return '{} LIKE \'%{}%\''.format(col, filter)


def build_query(operation, filters=None, orders=None):
    query = operation

    if filters is not None:
        query += ' WHERE {}'.format(filters[0])

        for i in range(1, len(filters) - 1):
            query += ' AND {}'.format(filters[i])

    if orders is not None:
        query += ' ORDER BY '

        for order in orders:
            query += order + ' '

    return '{};'.format(query)
