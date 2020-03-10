from app.sports.repositories import SportRepository
from app.tests.mocks import sport_repository


def configure(binder):
    binder.bind(
        SportRepository,
        to=sport_repository,
    )
