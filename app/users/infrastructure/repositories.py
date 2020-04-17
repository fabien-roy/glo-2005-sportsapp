import datetime

from injector import inject

from app.interfaces.database import Database
from app.recommendations.repositories import RecommendationRepository
from app.users.exceptions import UserNotFoundException
from app.users.infrastructure.queries import MySQLUserQuery as Query
from app.users.infrastructure.tables import MySQLUserTable as Users
from app.users.models import User
from app.users.repositories import UserRepository


class MySQLUserRepository(UserRepository):
    @inject
    def __init__(self, database: Database, recommendation_repository: RecommendationRepository):
        self.database = database
        self.recommendation_repository = recommendation_repository

    def get_all(self, form=None):
        all_users = []

        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_all(form)
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
            with self.database.connect().cursor() as cur:
                query = Query().get(username)
                cur.execute(query)

                for user_cur in cur.fetchall():
                    sport_recommendations = self.recommendation_repository\
                        .get_all_for_sport_and_user(username)
                    practice_center_recommendations = self.recommendation_repository\
                        .get_all_for_practice_center_and_user(username)
                    user = self.build_user(user_cur, sport_recommendations,
                                           practice_center_recommendations)
        finally:
            cur.close()

        if user is None:
            raise UserNotFoundException

        return user

    @staticmethod
    def build_user(cur, sport_recommendations=None, practice_center_recommendations=None):
        return User(cur[Users.username_col],
                    cur[Users.email_col],
                    cur[Users.first_name_col],
                    cur[Users.last_name_col],
                    cur[Users.phone_number_col],
                    cur[Users.creation_date_col],
                    cur[Users.last_login_date_col],
                    sport_recommendations,
                    practice_center_recommendations)

    def add(self, user):
        try:
            with self.database.connect().cursor() as cur:
                user.creation_date = datetime.datetime.now()

                query = Query().add()
                cur.execute(query, (user.username, user.email, user.first_name, user.last_name,
                                    user.phone_number, user.creation_date))

                self.database.connect().commit()
        finally:
            cur.close()

        return cur.lastrowid