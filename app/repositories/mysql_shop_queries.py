from app.repositories.mysql_queries import build_query


class MySQLShopsQuery:
    table_name = 'shops'

    id_col = 'id'
    location_id_col = 'location_id'
    name_col = 'name'
    email_col = 'email'
    phone_number_col = 'phone_number'
    web_site_col = 'web_site'

    def add(self):
        operation = ('INSERT INTO ' + self.table_name +
                     ' (' + self.id_col + ', ' + self.location_id_col + ', ' + self.name_col +
                     ', ' + self.email_col + ', ' + self.phone_number_col + ', ' + self.web_site_col + ')' +
                     ' VALUES (%s, %s, %s, %s, %s, %s);')

        return build_query(operation)
