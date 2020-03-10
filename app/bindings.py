from app.practice_centers.repositories import PracticeCenterRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCenterRepository
from app.repositories.mysql_sport_repositories import MySQLSportRepository
from app.sports.repositories import SportRepository


def configure(binder):
    binder.bind(
        SportRepository,
        to=MySQLSportRepository(),
    )
    binder.bind(
        PracticeCenterRepository,
        to=MySQLPracticeCenterRepository(),
    )
