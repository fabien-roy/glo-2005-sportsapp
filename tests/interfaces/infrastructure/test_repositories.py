import unittest

from app.announces.infrastructure.repositories import MySQLAnnounceRepository
from app.climates.infrastructure.repositories import MySQLClimateRepository
from app.equipments.infrastructure.repositories import MySQLEquipmentRepository
from app.practice_centers.infrastructure.repositories import MySQLPracticeCenterRepository
from app.recommendations.infrastructure.repositories import MySQLRecommendationRepository
from app.shops.infrastructure.repositories import MySQLShopRepository
from app.sports.infrastructure.repositories import MySQLSportRepository
from app.users.infrastructure.repositories import MySQLUserRepository
from instance.db_create import db_create
from tests.announces.fakes import shop1_equipment1_announce1, shop1_equipment2_announce1, \
    shop2_equipment2_announce1, shop2_equipment2_announce2, shop3_equipment1_announce1, \
    shop3_equipment3_announce1
from tests.climates.fakes import climate1, climate2, climate3
from tests.interfaces import test_basic
from tests.interfaces.infrastructure.database import test_database
from tests.practice_centers.fakes import center1, center2, center3
from tests.recommendations.fakes import sport1_recommendation1_user1, \
    sport2_recommendation1_user3, sport2_recommendation2_user2, sport3_recommendation1_user1, \
    center1_recommendation1_user1, center2_recommendation1_user1, center2_recommendation2_user2, \
    center3_recommendation1_user3, center3_recommendation2_user1
from tests.shops.fakes import shop1, shop2, shop3
from tests.sports.fakes import sport1, sport2, sport3
from tests.users.fakes import user1, user2, user3
from tests.equipments.fakes import equipment1, equipment2, equipment3


class RepositoryTests(test_basic.BasicTests):
    database_populated = False

    climates_repository = MySQLClimateRepository(test_database)
    recommendations_repository = MySQLRecommendationRepository(test_database)
    sports_repository = MySQLSportRepository(test_database, climates_repository,
                                             recommendations_repository)
    practice_centers_repository = MySQLPracticeCenterRepository(test_database, climates_repository,
                                                                recommendations_repository)
    announces_repository = MySQLAnnounceRepository(test_database)
    shops_repository = MySQLShopRepository(test_database, announces_repository)
    equipments_repository = MySQLEquipmentRepository(test_database, announces_repository)
    users_repository = MySQLUserRepository(test_database, recommendations_repository)

    @classmethod
    def setUpClass(cls):
        cls.recreate_database()
        cls.populate_database()

    @classmethod
    def recreate_database(cls):
        db_create(test_database)
        cls.database_populated = False

    @classmethod
    def populate_database(cls):
        cls.add_climates()
        cls.add_sports()
        cls.add_practice_centers()
        cls.add_users()
        cls.add_sport_recommendations()
        cls.add_practice_center_recommendations()
        cls.add_shops()
        cls.add_equipments()
        cls.add_announces()
        cls.database_populated = True

    @classmethod
    def add_climates(cls):
        cls.climates_repository.add(climate1)
        cls.climates_repository.add(climate2)
        cls.climates_repository.add(climate3)

    @classmethod
    def add_sports(cls):
        cls.sports_repository.add(sport1)
        cls.sports_repository.add(sport2)
        cls.sports_repository.add(sport3)

    @classmethod
    def add_practice_centers(cls):
        cls.practice_centers_repository.add(center1)
        cls.practice_centers_repository.add(center2)
        cls.practice_centers_repository.add(center3)

    @classmethod
    def add_users(cls):
        cls.users_repository.add(user1)
        cls.users_repository.add(user2)
        cls.users_repository.add(user3)

    @classmethod
    def add_sport_recommendations(cls):
        cls.recommendations_repository.add_for_sport(sport1_recommendation1_user1, sport1)
        cls.recommendations_repository.add_for_sport(sport2_recommendation1_user3, sport2)
        cls.recommendations_repository.add_for_sport(sport2_recommendation2_user2, sport2)
        cls.recommendations_repository.add_for_sport(sport3_recommendation1_user1, sport3)

    @classmethod
    def add_practice_center_recommendations(cls):
        cls.recommendations_repository.add_for_practice_center(center1_recommendation1_user1,
                                                               center1)
        cls.recommendations_repository.add_for_practice_center(center2_recommendation1_user1,
                                                               center2)
        cls.recommendations_repository.add_for_practice_center(center2_recommendation2_user2,
                                                               center2)
        cls.recommendations_repository.add_for_practice_center(center3_recommendation1_user3,
                                                               center3)
        cls.recommendations_repository.add_for_practice_center(center3_recommendation2_user1,
                                                               center3)

    @classmethod
    def add_shops(cls):
        cls.shops_repository.add(shop1)
        cls.shops_repository.add(shop2)
        cls.shops_repository.add(shop3)

    @classmethod
    def add_equipments(cls):
        cls.equipments_repository.add(equipment1)
        cls.equipments_repository.add(equipment2)
        cls.equipments_repository.add(equipment3)

    @classmethod
    def add_announces(cls):
        cls.announces_repository.add(shop1_equipment1_announce1, shop1, equipment1)
        cls.announces_repository.add(shop1_equipment2_announce1, shop1, equipment2)
        cls.announces_repository.add(shop2_equipment2_announce1)
        cls.announces_repository.add(shop2_equipment2_announce2)
        cls.announces_repository.add(shop3_equipment1_announce1)
        cls.announces_repository.add(shop3_equipment3_announce1)

    def tearDown(self):
        if not self.database_populated:
            self.populate_database()


if __name__ == "__main__":
    unittest.main()
