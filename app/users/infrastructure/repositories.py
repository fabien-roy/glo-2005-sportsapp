from datetime import datetime

from injector import inject
import bcrypt

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

    def get_all(self, form=None, offset=None, per_page=None):
        all_users = []

        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_all(form, offset, per_page)
                cur.execute(query)

                for user_cur in cur.fetchall():
                    user = self.build_user(user_cur)
                    all_users.append(user)
        finally:
            cur.close()

        return all_users

    def get_count(self, form=None):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_count(form)
                cur.execute(query)

                for user_cur in cur.fetchall():
                    return user_cur[Query.fake_count_col]
        finally:
            cur.close()

        return 0

    def get(self, username):
        user = None

        try:
            with self.database.connect().cursor() as cur:
                query = Query().get(username)
                cur.execute(query)

                for user_cur in cur.fetchall():
                    sport_recommendations = self.recommendation_repository \
                        .get_all_for_sport_and_user(username)
                    practice_center_recommendations = self.recommendation_repository \
                        .get_all_for_practice_center_and_user(username)
                    user = self.build_user(user_cur, sport_recommendations,
                                           practice_center_recommendations)
        finally:
            cur.close()

        if user is None:
            raise UserNotFoundException

        return user

    def get_touch(self, username):
        user = self.get(username)
        user.last_login_date = datetime.now()

        try:
            with self.database.connect().cursor() as cur:
                query = Query().update_last_login_date(user.username, user.last_login_date)
                cur.execute(query)

                self.database.connect().commit()
        finally:
            cur.close()

        return user

    @staticmethod
    def build_user(cur, sport_recommendations=None, practice_center_recommendations=None):
        return User(username=cur[Users.username_col],
                    email=cur[Users.email_col],
                    first_name=cur[Users.first_name_col],
                    last_name=cur[Users.last_name_col],
                    phone_number=cur[Users.phone_number_col],
                    creation_date=cur[Users.creation_date_col],
                    last_login_date=cur[Users.last_login_date_col],
                    sport_recommendations=sport_recommendations,
                    practice_center_recommendations=practice_center_recommendations)

    def add(self, user):
        try:
            with self.database.connect().cursor() as cur:
                user.creation_date = datetime.now()

                query = Query().add()
                cur.execute(query, (user.username, user.email, user.first_name, user.last_name,
                                    user.phone_number, user.creation_date))

                self.database.connect().commit()
        finally:
            cur.close()

        self.add_password(user)

        return cur.lastrowid

    def add_password(self, user):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().add_password()
                cur.execute(query, (
                    user.username, bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())))
                self.database.connect().commit()
        finally:
            cur.close()

        return cur.lastrowid

    def get_password(self, username):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_password(username)
                cur.execute(query)
                password = cur.fetchall()[0]['password']
        finally:
            cur.close()

        return password
