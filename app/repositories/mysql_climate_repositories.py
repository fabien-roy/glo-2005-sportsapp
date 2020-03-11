from app import conn
from app.climates.repositories import ClimateRepository


class MySQLClimateRepository(ClimateRepository):
    table_name = 'climates'

    name_col = 'name'

    def add(self, climate):
        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.name_col + ')' +
                       ' VALUES (%s);')
                cur.execute(sql, climate.name)

                conn.commit()
        finally:
            cur.close()

        return cur.lastrowid
