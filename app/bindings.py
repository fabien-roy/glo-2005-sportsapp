from app.announces.infrastructure.repositories import MySQLAnnounceRepository
from app.announces.repositories import AnnounceRepository
from app.climates.infrastructure.repositories import MySQLClimateRepository
from app.climates.repositories import ClimateRepository
from app.equipments.infrastructure.repositories import MySQLEquipmentRepository
from app.interfaces.database import Database
from app.interfaces.infrastructure.database import MySQLDatabase
from app.practice_centers.infrastructure.repositories import MySQLPracticeCenterRepository
from app.practice_centers.repositories import PracticeCenterRepository
from app.equipments.repositories import EquipmentRepository
from app.recommendations.infrastructure.repositories import MySQLRecommendationRepository
from app.recommendations.repositories import RecommendationRepository
from app.shops.infrastructure.repositories import MySQLShopRepository
from app.shops.repositories import ShopsRepository
from app.sports.infrastructure.repositories import MySQLSportRepository
from app.sports.repositories import SportRepository
from app.users.infrastructure.repositories import MySQLUserRepository
from app.users.repositories import UsersRepository


def configure(binder):
    binder.bind(Database, to=MySQLDatabase)

    binder.bind(ClimateRepository, to=MySQLClimateRepository)
    binder.bind(RecommendationRepository, to=MySQLRecommendationRepository)
    binder.bind(SportRepository, to=MySQLSportRepository)
    binder.bind(PracticeCenterRepository, to=MySQLPracticeCenterRepository)
    binder.bind(AnnounceRepository, to=MySQLAnnounceRepository)
    binder.bind(ShopsRepository, to=MySQLShopRepository)
    binder.bind(EquipmentRepository, to=MySQLEquipmentRepository)
    binder.bind(UsersRepository, to=MySQLUserRepository)
