from app.repositories.mysql_queries import build_query, filter_equal, filter_like


class MySQLPracticeCentersQuery:
    table_name = 'practice_centers'

    id_col = 'id'
    name_col = 'name'
    email_col = 'email'
    web_site_col = 'web_site'
    phone_number_col = 'phone_number'

    def get_all(self, form=None):
        operation = ('SELECT ' + self.id_col + ', ' + self.name_col + ', ' + self.email_col + ', ' +
                     self.web_site_col + ', ' + self.phone_number_col +
                     ' FROM ' + self.table_name)

        inner_filtering = True

        if form is None:
            filters = None
        else:
            filters = []

            if form.all.data is not '':
                inner_filtering = False
                filters.append(filter_like(self.name_col, form.all.data))
                filters.append(filter_like(self.email_col, form.all.data))
                filters.append(filter_like(self.web_site_col, form.all.data))
                filters.append(filter_like(self.phone_number_col, form.all.data))
            else:
                if form.name.data is not '':
                    filters.append(filter_like(self.name_col, form.name.data))

                if form.email.data is not '':
                    filters.append(filter_like(self.email_col, form.email.data))

                if form.web_site.data is not '':
                    filters.append(filter_like(self.web_site_col, form.web_site.data))

                if form.phone_number.data is not '':
                    filters.append(filter_like(self.phone_number_col, form.phone_number.data))

        orders = [self.name_col]

        return build_query(operation, filters, orders, inner_filtering)

    def get(self, practice_center_id):
        operation = ('SELECT ' + self.id_col + ', ' + self.name_col + ', ' + self.email_col + ', ' +
                     self.web_site_col + ', ' + self.phone_number_col +
                     ' FROM ' + self.table_name)

        filters = [filter_equal(self.id_col, practice_center_id)]

        return build_query(operation, filters)

    def add(self):
        operation = ('INSERT INTO ' + self.table_name +
                     ' (' + self.name_col + ', ' + self.email_col + ', ' + self.web_site_col +
                     ', ' + self.phone_number_col + ')' +
                     ' VALUES (%s, %s, %s, %s);')

        return build_query(operation)
