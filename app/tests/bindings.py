from app.climates.repositories import ClimatesRepository
from app.practice_centers.repositories import PracticeCentersRepository
from app.recommendations.repositories import RecommendationsRepository
from app.sports.repositories import SportsRepository
from app.tests.mocks import sports_repository, practice_centers_repository, users_repository, climates_repository, \
    recommendations_repository
from app.users.repositories import UsersRepository


def configure(binder):
    binder.bind(ClimatesRepository, to=climates_repository)
    binder.bind(RecommendationsRepository, to=recommendations_repository)
    binder.bind(SportsRepository, to=sports_repository)
    binder.bind(PracticeCentersRepository, to=practice_centers_repository)
    binder.bind(UsersRepository, to=users_repository)
