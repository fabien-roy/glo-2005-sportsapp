from app.announces.repositories import AnnouncesRepository
from app.climates.climate_repository import ClimatesRepository
from app.database import Database
from app.practice_centers.repositories import PracticeCentersRepository
from app.equipments.repositories import EquipmentRepository
from app.recommendations.repositories import RecommendationRepository
from app.repositories.mysql_announce_repositories import MySQLAnnouncesRepository
from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_database import MySQLDatabase
from app.repositories.mysql_equipment_repositories import MySQLEquipmentsRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_shop_repositories import MySQLShopsRepository
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.shops.repositories import ShopsRepository
from app.sports.repositories import SportRepository
from app.users.repositories import UsersRepository


def configure(binder):
    binder.bind(Database, to=MySQLDatabase)

    binder.bind(ClimatesRepository, to=MySQLClimatesRepository)
    binder.bind(RecommendationRepository, to=MySQLRecommendationsRepository)
    binder.bind(SportRepository, to=MySQLSportsRepository)
    binder.bind(PracticeCentersRepository, to=MySQLPracticeCentersRepository)
    binder.bind(AnnouncesRepository, to=MySQLAnnouncesRepository)
    binder.bind(ShopsRepository, to=MySQLShopsRepository)
    binder.bind(EquipmentRepository, to=MySQLEquipmentsRepository)
    binder.bind(UsersRepository, to=MySQLUsersRepository)
