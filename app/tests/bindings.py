from app.climates.repositories import ClimatesRepository
from app.practice_centers.repositories import PracticeCentersRepository
from app.sports.repositories import SportsRepository
from app.tests.mocks import sports_repository, practice_centers_repository, users_repository, climates_repository
from app.users.repositories import UsersRepository


def configure(binder):
    binder.bind(
        SportsRepository,
        to=sports_repository,
    )
    binder.bind(
        PracticeCentersRepository,
        to=practice_centers_repository,
    )
    binder.bind(
        UsersRepository,
        to=users_repository,
    )
    binder.bind(
        ClimatesRepository,
        to=climates_repository,
    )
