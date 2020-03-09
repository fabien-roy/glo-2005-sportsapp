from app import conn
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
                            ' ORDER BY ' + self.name_col)

                for (sport_id, name) in cur.fetchall():
                    sport = Sport(sport_id, name)
                    all_sports.append(sport)
        finally:
            conn.close()

        return all_sports

    def get(self, sport_id):
        sport = Sport

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.id_col + ', ' + self.name_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.id_col + ' = %s')
                cur.execute(sql, sport_id)

                for (sport_id, name) in cur.fetchone():
                    sport = Sport(sport_id, name)
        finally:
            conn.close()

        return sport

    def add(self, sport):
        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.name_col + ')' +
                       ' VALUES (%s)')
                cur.execute(sql, sport.name)

                conn.commit()
        finally:
            conn.close()
