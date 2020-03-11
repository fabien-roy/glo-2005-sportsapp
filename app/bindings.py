from app.practice_centers.repositories import PracticeCenterRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCenterRepository
from app.repositories.mysql_sport_repositories import MySQLSportRepository
from app.repositories.mysql_user_repositories import MySQLUserRepository
from app.sports.repositories import SportRepository
from app.users.repositories import UserRepository


def configure(binder):
    binder.bind(
        SportRepository,
        to=MySQLSportRepository(),
    )
    binder.bind(
        PracticeCenterRepository,
        to=MySQLPracticeCenterRepository(),
    )
    binder.bind(
        UserRepository,
        to=MySQLUserRepository(),
    )
