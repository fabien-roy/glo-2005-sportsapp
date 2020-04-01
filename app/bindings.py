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
    binder.bind(ClimatesRepository, to=MySQLClimatesRepository())
    binder.bind(RecommendationsRepository, to=MySQLRecommendationsRepository())
    binder.bind(SportsRepository, to=MySQLSportsRepository())
    binder.bind(PracticeCentersRepository, to=MySQLPracticeCentersRepository())
    binder.bind(ShopsRepository, to=MySQLShopsRepository())
    binder.bind(UsersRepository, to=MySQLUsersRepository())
