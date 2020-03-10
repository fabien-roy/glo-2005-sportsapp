from app import conn
from app.exceptions import SportNotFoundException
from app.models import Sport


class UserQuery:
    table_name = 'users'

    username_col = 'username'
    email_col = 'email'
    password_col = 'password'  # TODO : Move password to another table
    first_name_col = 'first_name'
    last_name_col = 'last_name'
    telephone_col = 'telephone'

    # TODO : Rest of UserQuery


class SportQuery:
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
                       ' (' + self.name_col + ')' +
                       ' VALUES (%s);')
                cur.execute(sql, sport.name)

                conn.commit()
        finally:
            cur.close()
