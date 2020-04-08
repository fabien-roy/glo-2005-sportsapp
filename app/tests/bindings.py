from app.climates.repositories import ClimatesRepository
from app.practice_centers.repositories import PracticeCentersRepository
from app.recommendations.repositories import RecommendationsRepository
from app.shops.repositories import ShopsRepository
from app.sports.repositories import SportsRepository
from app.tests.climates.mocks import climates_repository
from app.tests.practice_centers.mocks import practice_centers_repository
from app.tests.recommendations.mocks import recommendations_repository
from app.tests.shops.mocks import shops_repository
from app.tests.sports.mocks import sports_repository
from app.tests.users.mocks import users_repository
from app.users.repositories import UsersRepository


def configure(binder):
    binder.bind(ClimatesRepository, to=climates_repository)
    binder.bind(RecommendationsRepository, to=recommendations_repository)
    binder.bind(SportsRepository, to=sports_repository)
    binder.bind(PracticeCentersRepository, to=practice_centers_repository)
    binder.bind(UsersRepository, to=users_repository)
    binder.bind(ShopsRepository, to=shops_repository)
