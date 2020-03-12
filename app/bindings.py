from app.practice_centers.repositories import PracticeCentersRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.sports.repositories import SportsRepository
from app.users.repositories import UsersRepository


def configure(binder):
    binder.bind(
        SportsRepository,
        to=MySQLSportsRepository(),
    )
    binder.bind(
        PracticeCentersRepository,
        to=MySQLPracticeCentersRepository(),
    )
    binder.bind(
        UsersRepository,
        to=MySQLUsersRepository(),
    )
