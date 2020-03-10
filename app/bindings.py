from app.repositories.mysql_sport_repositories import MySQLSportRepository
from app.sports.repositories import SportRepository


def configure(binder):
    binder.bind(
        SportRepository,
        to=MySQLSportRepository(),
    )
