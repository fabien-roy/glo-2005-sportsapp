import datetime

from app import conn
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_tables import MySQLUsersTable
from app.repositories.mysql_user_queries import MySQLUsersQuery
from app.users.exceptions import UserNotFoundException
from app.users.models import User
from app.users.repositories import UsersRepository


class MySQLUsersRepository(UsersRepository):
    # TODO : Inject in repositories
    recommendation_repository = MySQLRecommendationsRepository()

    def get_all(self, form=None):
        all_users = []

        try:
            with conn.cursor() as cur:
                query = MySQLUsersQuery().get_all(form)
                cur.execute(query)

                for user_cur in cur.fetchall():
                    user = self.build_user(user_cur)
                    all_users.append(user)
        finally:
            cur.close()

        return all_users

    def get(self, username):
        user = None

        try:
            with conn.cursor() as cur:
                query = MySQLUsersQuery().get(username)
                cur.execute(query)

                # TODO : Use fetchone (causes integer error)
                for user_cur in cur.fetchall():
                    sport_recommendations = self.recommendation_repository.get_sport_recommendations_for_user(username)
                    practice_center_recommendations = \
                        self.recommendation_repository.get_practice_center_recommendations_for_user(username)
                    user = self.build_user(user_cur, sport_recommendations, practice_center_recommendations)
        finally:
            cur.close()

        if user is None:
            raise UserNotFoundException

        return user

    @staticmethod
    def build_user(cur, sport_recommendations=None, practice_center_recommendations=None):
        return User(cur[MySQLUsersTable.username_col],
                    cur[MySQLUsersTable.email_col],
                    cur[MySQLUsersTable.first_name_col],
                    cur[MySQLUsersTable.last_name_col],
                    cur[MySQLUsersTable.phone_number_col],
                    cur[MySQLUsersTable.creation_date_col],
                    cur[MySQLUsersTable.last_login_date_col],
                    sport_recommendations,
                    practice_center_recommendations)

    def add(self, user):
        try:
            with conn.cursor() as cur:
                user.creation_date = datetime.datetime.now()

                query = MySQLUsersQuery().add()
                cur.execute(query, (user.username, user.email, user.first_name, user.last_name, user.phone_number,
                                    user.creation_date))

                conn.commit()
        finally:
            cur.close()

        return cur.lastrowid
