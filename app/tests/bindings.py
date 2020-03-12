from app.practice_centers.repositories import PracticeCentersRepository
from app.sports.repositories import SportsRepository
from app.tests.mocks import sport_repository, practice_center_repository, user_repository
from app.users.repositories import UsersRepository


def configure(binder):
    binder.bind(
        SportsRepository,
        to=sport_repository,
    )
    binder.bind(
        PracticeCentersRepository,
        to=practice_center_repository,
    )
    binder.bind(
        UsersRepository,
        to=user_repository,
    )
