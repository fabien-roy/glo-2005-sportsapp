from app.climates.repositories import ClimatesRepository
from app.practice_centers.repositories import PracticeCentersRepository
from app.equipments.repositories import EquipmentsRepository
from app.recommendations.repositories import RecommendationsRepository
from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_database import MySQLDatabase
from app.repositories.mysql_equipment_repositories import MySQLEquipmentsRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_shop_repositories import MySQLShopsRepository
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.shops.repositories import ShopsRepository
from app.sports.repositories import SportsRepository
from app.users.repositories import UsersRepository


def configure(binder):
    database = MySQLDatabase()

    climates_repository = MySQLClimatesRepository(database)
    recommendations_repository = MySQLRecommendationsRepository(database)
    sports_repository = MySQLSportsRepository(database, climates_repository,
                                              recommendations_repository)
    practice_centers_repository = MySQLPracticeCentersRepository(database, climates_repository,
                                                                 recommendations_repository)
    shops_repository = MySQLShopsRepository(database)
    equipments_repository = MySQLEquipmentsRepository(database)
    users_repository = MySQLUsersRepository(database, recommendations_repository)

    binder.bind(ClimatesRepository, to=climates_repository)
    binder.bind(RecommendationsRepository, to=recommendations_repository)
    binder.bind(SportsRepository, to=sports_repository)
    binder.bind(PracticeCentersRepository, to=practice_centers_repository)
    binder.bind(ShopsRepository, to=shops_repository)
    binder.bind(EquipmentsRepository, to=equipments_repository)
    binder.bind(UsersRepository, to=users_repository)
