import unittest

from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.repositories.mysql_shop_repositories import MySQLShopsRepository
from app.tests import test_basic
from app.tests.climates.fakes import climate1, climate2, climate3
from app.tests.practice_centers.fakes import center1, center2, center3
from app.tests.recommendations.fakes import sport1_recommendation1_user1, sport2_recommendation1_user3, \
    sport2_recommendation2_user2, sport3_recommendation1_user1, center1_recommendation1_user1, \
    center2_recommendation1_user1, center2_recommendation2_user2, center3_recommendation1_user3, \
    center3_recommendation2_user1
from app.tests.sports.fakes import sport1, sport2, sport3
from app.tests.users.fakes import user1, user2, user3
from app.tests.shops.fakes import shop1, shop2, shop3
from instance.db_create import db_create


class BasicRepositoryTests(test_basic.BasicTests):
    climates_repository = MySQLClimatesRepository()
    recommendations_repository = MySQLRecommendationsRepository()
    sports_repository = MySQLSportsRepository(climates_repository, recommendations_repository)
    practice_centers_repository = MySQLPracticeCentersRepository(climates_repository, recommendations_repository)
    users_repository = MySQLUsersRepository(recommendations_repository)
    shops_repository = MySQLShopsRepository()

    def setUp(self):
        super().setUp()
        self.reset_repositories()
        self.add_climates()
        self.add_sports()
        self.add_practice_centers()
        self.add_users()
        self.add_sport_recommendations()
        self.add_practice_center_recommendations()
        self.add_shops()

    @staticmethod
    def reset_repositories():
        db_create()

    def add_climates(self):
        self.climates_repository.add(climate1)
        self.climates_repository.add(climate2)
        self.climates_repository.add(climate3)

    def add_sports(self):
        self.sports_repository.add(sport1)
        self.sports_repository.add(sport2)
        self.sports_repository.add(sport3)

    def add_practice_centers(self):
        self.practice_centers_repository.add(center1)
        self.practice_centers_repository.add(center2)
        self.practice_centers_repository.add(center3)

    def add_users(self):
        self.users_repository.add(user1)
        self.users_repository.add(user2)
        self.users_repository.add(user3)

    def add_sport_recommendations(self):
        self.recommendations_repository.add_for_sport(sport1_recommendation1_user1, sport1)
        self.recommendations_repository.add_for_sport(sport2_recommendation1_user3, sport2)
        self.recommendations_repository.add_for_sport(sport2_recommendation2_user2, sport2)
        self.recommendations_repository.add_for_sport(sport3_recommendation1_user1, sport3)

    def add_practice_center_recommendations(self):
        self.recommendations_repository.add_for_practice_center(center1_recommendation1_user1, center1)
        self.recommendations_repository.add_for_practice_center(center2_recommendation1_user1, center2)
        self.recommendations_repository.add_for_practice_center(center2_recommendation2_user2, center2)
        self.recommendations_repository.add_for_practice_center(center3_recommendation1_user3, center3)
        self.recommendations_repository.add_for_practice_center(center3_recommendation2_user1, center3)

    def add_shops(self):
        self.shops_repository.add(shop1)
        self.shops_repository.add(shop2)
        self.shops_repository.add(shop3)


if __name__ == "__main__":
    unittest.main()
