from app.announces.repositories import AnnounceRepository
from app.climates.repositories import ClimateRepository
from app.interfaces.database import Database
from app.practice_centers.repositories import PracticeCenterRepository
from app.recommendations.repositories import RecommendationRepository
from app.shops.repositories import ShopRepository
from app.sports.repositories import SportRepository
from app.users.repositories import UserRepository
from app.equipments.repositories import EquipmentRepository
from tests.announces.mocks import announce_repository
from tests.climates.mocks import climate_repository
from tests.practice_centers.mocks import practice_center_repository
from tests.recommendations.mocks import recommendation_repository
from tests.repositories.mysql_test_database import test_database
from tests.shops.mocks import shop_repository
from tests.sports.mocks import sport_repository
from tests.users.mocks import user_repository
from tests.equipments.mocks import equipment_repository


def configure(binder):
    binder.bind(Database, to=test_database)
    binder.bind(ClimateRepository, to=climate_repository)
    binder.bind(RecommendationRepository, to=recommendation_repository)
    binder.bind(SportRepository, to=sport_repository)
    binder.bind(PracticeCenterRepository, to=practice_center_repository)
    binder.bind(AnnounceRepository, to=announce_repository)
    binder.bind(ShopRepository, to=shop_repository)
    binder.bind(EquipmentRepository, to=equipment_repository)
    binder.bind(UserRepository, to=user_repository)
