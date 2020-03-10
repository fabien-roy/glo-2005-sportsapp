from app import conn
from app.sports.models import Sport
from app.sports.exceptions import SportNotFoundException
from app.sports.repositories import SportRepository


class MySQLSportRepository(SportRepository):
    table_name = 'sports'

    id_col = 'id'
    name_col = 'name'

    def get_all(self):
        all_sports = []

        try:
            with conn.cursor() as cur:
                cur.execute('SELECT ' + self.id_col + ', ' + self.name_col +
                            ' FROM ' + self.table_name +
                            ' ORDER BY ' + self.name_col + ';')

                for sport_cur in cur.fetchall():
                    sport = Sport(sport_cur[self.id_col], sport_cur[self.name_col])
                    all_sports.append(sport)
        finally:
            cur.close()

        return all_sports

    def get(self, sport_id):
        sport = None

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.id_col + ', ' + self.name_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.id_col + ' = %s;')
                cur.execute(sql, sport_id)

                # TODO : Use fetchone (causes integer error)
                for sport_cur in cur.fetchall():
                    sport = Sport(sport_cur[self.id_col], sport_cur[self.name_col])
        finally:
            cur.close()

        if sport is None:
            raise SportNotFoundException

        return sport

    def add(self, sport):
        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.id_col + ', ' + self.name_col + ')' +
                       ' VALUES (%s, %s);')
                cur.execute(sql, (sport.id, sport.name))

                conn.commit()
        finally:
            cur.close()
