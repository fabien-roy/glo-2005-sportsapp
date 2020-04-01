from app.climates.repositories import ClimatesRepository
from app.practice_centers.repositories import PracticeCentersRepository
from app.recommendations.repositories import RecommendationsRepository
from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_shop_repositories import MySQLShopsRepository
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.shops.repositories import ShopsRepository
from app.sports.repositories import SportsRepository
from app.users.repositories import UsersRepository


def configure(binder):
    climate_repository = MySQLClimatesRepository()
    recommendation_repository = MySQLRecommendationsRepository()
    sport_repository = MySQLSportsRepository(climate_repository, recommendation_repository)
    practice_center_repository = MySQLPracticeCentersRepository(climate_repository, recommendation_repository)
    user_repository = MySQLUsersRepository(recommendation_repository)
    shop_repository = MySQLShopsRepository()

    binder.bind(ClimatesRepository, to=climate_repository)
    binder.bind(RecommendationsRepository, to=recommendation_repository)
    binder.bind(SportsRepository, to=sport_repository)
    binder.bind(PracticeCentersRepository, to=practice_center_repository)
    binder.bind(UsersRepository, to=user_repository)
    binder.bind(ShopsRepository, to=shop_repository)
