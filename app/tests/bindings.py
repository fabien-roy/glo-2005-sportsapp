from app.practice_centers.repositories import PracticeCenterRepository
from app.sports.repositories import SportRepository
from app.tests.mocks import sport_repository, practice_center_repository


def configure(binder):
    binder.bind(
        SportRepository,
        to=sport_repository,
    )
    binder.bind(
        PracticeCenterRepository,
        to=practice_center_repository,
    )
