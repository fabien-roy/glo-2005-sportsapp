from app.practice_centers.repositories import PracticeCenterRepository
from app.sports.repositories import SportRepository
from app.tests.mocks import sport_repository, practice_center_repository, user_repository
from app.users.repositories import UserRepository


def configure(binder):
    binder.bind(
        SportRepository,
        to=sport_repository,
    )
    binder.bind(
        PracticeCenterRepository,
        to=practice_center_repository,
    )
    binder.bind(
        UserRepository,
        to=user_repository,
    )
