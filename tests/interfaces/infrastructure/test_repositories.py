from app.announces.infrastructure.repositories import MySQLAnnounceRepository
from app.bindings import configure_modules
from app.equipment_types.infrastructure.repositories import MySQLEquipmentTypeRepository
from app.climates.infrastructure.repositories import MySQLClimateRepository
from app.manufacturers.infrastructure.repositories import MySQLManufacturerRepository
from app.equipments.infrastructure.repositories import MySQLEquipmentRepository
from app.practice_centers.infrastructure.repositories import MySQLPracticeCenterRepository
from app.recommendations.infrastructure.repositories import MySQLRecommendationRepository
from app.shops.infrastructure.repositories import MySQLShopRepository
from app.sports.infrastructure.repositories import MySQLSportRepository
from app.users.infrastructure.repositories import MySQLUserRepository
from instance import instance
from instance.injectors import InstanceInjector
from tests.manufacturers.fakes import manufacturer1, manufacturer2, manufacturer3
from tests.equipment_types.fakes import type1, type2, type3
from tests.announces.fakes import shop1_equipment1_announce1, shop1_equipment2_announce1, \
    shop2_equipment2_announce1, shop2_equipment2_announce2, shop3_equipment1_announce1, \
    shop3_equipment3_announce1
from tests.bindings import configure_test_database
from tests.climates.fakes import climate1, climate2, climate3
from tests.equipments.fakes import equipment1, equipment2, equipment3
from tests.interfaces.infrastructure.database import test_database
from tests.interfaces.test_basic import BasicTests
from tests.practice_centers.fakes import center1, center2, center3
from tests.recommendations.fakes import sport1_recommendation1_user1, \
    sport2_recommendation1_user3, sport2_recommendation2_user2, sport3_recommendation1_user1, \
    center1_recommendation1_user1, center2_recommendation1_user1, center2_recommendation2_user2, \
    center3_recommendation1_user3, center3_recommendation2_user1
from tests.shops.fakes import shop1, shop2, shop3
from tests.sports.fakes import sport1, sport2, sport3
from tests.users.fakes import user1, user2, user3


class RepositoryTests(BasicTests):
    database_populated = False

    climate_repository = MySQLClimateRepository(test_database)
    recommendation_repository = MySQLRecommendationRepository(test_database)
    equipment_type_repository = MySQLEquipmentTypeRepository(test_database)

    sport_repository = MySQLSportRepository(test_database, climate_repository,
                                            equipment_type_repository,
                                            recommendation_repository)
    practice_center_repository = MySQLPracticeCenterRepository(test_database, climate_repository,
                                                               recommendation_repository)

    announce_repository = MySQLAnnounceRepository(test_database)
    manufacturer_repository = MySQLManufacturerRepository(test_database)
    equipment_repository = MySQLEquipmentRepository(test_database, sport_repository,
                                                    announce_repository)
    shop_repository = MySQLShopRepository(test_database, announce_repository)

    user_repository = MySQLUserRepository(test_database, recommendation_repository)

    @classmethod
    def setUpClass(cls):
        InstanceInjector(instance=instance, modules=[configure_test_database, configure_modules])
        cls.recreate_database()
        cls.populate_database()

    @classmethod
    def recreate_database(cls):
        instance.db_create()
        cls.database_populated = False

    @classmethod
    def populate_database(cls):
        cls.add_users()

        cls.add_shops()
        cls.add_manufacturers()
        cls.add_equipment_types()
        cls.add_equipments()
        cls.add_announces()

        cls.add_climates()

        cls.add_sports()
        cls.add_practice_centers()

        cls.add_sport_recommendations()
        cls.add_practice_center_recommendations()

        cls.database_populated = True

    @classmethod
    def add_users(cls):
        cls.user_repository.add(user1)
        cls.user_repository.add(user2)
        cls.user_repository.add(user3)

    @classmethod
    def add_shops(cls):
        cls.shop_repository.add(shop1)
        cls.shop_repository.add(shop2)
        cls.shop_repository.add(shop3)

    @classmethod
    def add_manufacturers(cls):
        cls.manufacturer_repository.add(manufacturer1)
        cls.manufacturer_repository.add(manufacturer2)
        cls.manufacturer_repository.add(manufacturer3)

    @classmethod
    def add_equipment_types(cls):
        cls.equipment_type_repository.add(type1)
        cls.equipment_type_repository.add(type2)
        cls.equipment_type_repository.add(type3)

    @classmethod
    def add_equipments(cls):
        cls.equipment_repository.add(equipment1)
        cls.equipment_repository.add(equipment2)
        cls.equipment_repository.add(equipment3)

    @classmethod
    def add_announces(cls):
        cls.announce_repository.add(shop1_equipment1_announce1, shop1.id, equipment1.id)
        cls.announce_repository.add(shop1_equipment2_announce1, shop1.id, equipment2.id)
        cls.announce_repository.add(shop2_equipment2_announce1, shop2.id, equipment2.id)
        cls.announce_repository.add(shop2_equipment2_announce2, shop2.id, equipment2.id)
        cls.announce_repository.add(shop3_equipment1_announce1, shop3.id, equipment1.id)
        cls.announce_repository.add(shop3_equipment3_announce1, shop3.id, equipment3.id)

    @classmethod
    def add_climates(cls):
        cls.climate_repository.add(climate1)
        cls.climate_repository.add(climate2)
        cls.climate_repository.add(climate3)

    @classmethod
    def add_sports(cls):
        cls.sport_repository.add(sport1)
        cls.sport_repository.add(sport2)
        cls.sport_repository.add(sport3)

    @classmethod
    def add_practice_centers(cls):
        cls.practice_center_repository.add(center1)
        cls.practice_center_repository.add(center2)
        cls.practice_center_repository.add(center3)

    @classmethod
    def add_sport_recommendations(cls):
        cls.recommendation_repository.add_to_sport(sport1_recommendation1_user1, sport1.id)
        cls.recommendation_repository.add_to_sport(sport2_recommendation1_user3, sport2.id)
        cls.recommendation_repository.add_to_sport(sport2_recommendation2_user2, sport2.id)
        cls.recommendation_repository.add_to_sport(sport3_recommendation1_user1, sport3.id)

    @classmethod
    def add_practice_center_recommendations(cls):
        cls.recommendation_repository.add_to_practice_center(center1_recommendation1_user1,
                                                             center1.id)
        cls.recommendation_repository.add_to_practice_center(center2_recommendation1_user1,
                                                             center2.id)
        cls.recommendation_repository.add_to_practice_center(center2_recommendation2_user2,
                                                             center2.id)
        cls.recommendation_repository.add_to_practice_center(center3_recommendation1_user3,
                                                             center3.id)
        cls.recommendation_repository.add_to_practice_center(center3_recommendation2_user1,
                                                             center3.id)

    def tearDown(self):
        if not self.database_populated:
            self.populate_database()
