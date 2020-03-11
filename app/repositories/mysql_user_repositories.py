import datetime

from app import conn
from app.users.exceptions import UserNotFoundException
from app.users.models import User
from app.users.repositories import UserRepository


class MySQLUserRepository(UserRepository):
    table_name = 'users'

    username_col = 'username'
    email_col = 'email'
    first_name_col = 'first_name'
    last_name_col = 'last_name'
    phone_number_col = 'phone_number'
    creation_date_col = 'creation_date'
    last_login_date_col = 'last_login_date'

    def get_all(self):
        all_users = []

        try:
            with conn.cursor() as cur:
                cur.execute('SELECT ' + self.username_col + ', ' + self.email_col +
                            ' FROM ' + self.table_name +
                            ' ORDER BY ' + self.username_col + ';')

                for user_cur in cur.fetchall():
                    user = User(user_cur[self.username_col], user_cur[self.email_col])
                    all_users.append(user)
        finally:
            cur.close()

        return all_users

    def get(self, username):
        user = None

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.username_col + ', ' + self.email_col + ', ' + self.first_name_col + ', ' +
                       self.last_name_col + ', ' + self.phone_number_col + ', ' + self.creation_date_col + ', ' +
                       self.last_login_date_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.username_col + ' = %s;')
                cur.execute(sql, username)

                # TODO : Use fetchone (causes integer error)
                for user_cur in cur.fetchall():
                    user = User(user_cur[self.username_col], user_cur[self.email_col], user_cur[self.first_name_col],
                                user_cur[self.last_name_col], user_cur[self.phone_number_col],
                                user_cur[self.creation_date_col], user_cur[self.last_login_date_col])
        finally:
            cur.close()

        if user is None:
            raise UserNotFoundException

        return user

    def add(self, user):
        try:
            with conn.cursor() as cur:
                user.creation_date = datetime.datetime.now()

                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.username_col + ', ' + self.email_col + ', ' + self.first_name_col + ', ' +
                       self.last_name_col + ', ' + self.phone_number_col + ', ' + self.creation_date_col + ')' +
                       ' VALUES (%s, %s, %s, %s, %s, %s);')
                cur.execute(sql, (user.username, user.email, user.first_name, user.last_name, user.phone_number,
                                  user.creation_date))

                conn.commit()
        finally:
            cur.close()

        return cur.lastrowid
