from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.tests import test_basic
from app.tests.fakes import climate1, climate2, climate3, user2, \
    user1, user3, sport1, sport2, sport3, sport1_recommendation1_user1, sport2_recommendation1_user3, \
    sport2_recommendation2_user2, sport3_recommendation1_user1
from instance.db_create import db_create


class BasicRepositoryTests(test_basic.BasicTests):
    sport_repository = MySQLSportsRepository()
    practice_center_repository = MySQLPracticeCentersRepository()
    climate_repository = MySQLClimatesRepository()
    recommendation_repository = MySQLRecommendationsRepository()
    user_repository = MySQLUsersRepository()

    @staticmethod
    def reset_repositories():
        db_create()

    def add_sports(self):
        self.reset_repositories()
        self.add_climates()
        self.sport_repository.add(sport1)
        self.sport_repository.add(sport2)
        self.sport_repository.add(sport3)

    def add_sports_recommendations(self):
        self.reset_repositories()
        self.add_sports()
        self.add_users()
        self.recommendation_repository.add_for_sport(sport1_recommendation1_user1, sport1)
        self.recommendation_repository.add_for_sport(sport2_recommendation1_user3, sport2)
        self.recommendation_repository.add_for_sport(sport2_recommendation2_user2, sport2)
        self.recommendation_repository.add_for_sport(sport3_recommendation1_user1, sport3)

    def add_climates(self):
        self.climate_repository.add(climate1)
        self.climate_repository.add(climate2)
        self.climate_repository.add(climate3)

    def add_users(self):
        self.user_repository.add(user1)
        self.user_repository.add(user2)
        self.user_repository.add(user3)
