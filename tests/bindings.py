from app.announces.repositories import AnnouncesRepository
from app.climates.climate_repository import ClimatesRepository
from app.database import Database
from app.practice_centers.repositories import PracticeCentersRepository
from app.recommendations.repositories import RecommendationRepository
from app.shops.repositories import ShopsRepository
from app.sports.repositories import SportRepository
from app.users.repositories import UsersRepository
from app.equipments.repositories import EquipmentRepository
from tests.announces.mocks import announces_repository
from tests.climates.mocks import climates_repository
from tests.practice_centers.mocks import practice_centers_repository
from tests.recommendations.mocks import recommendations_repository
from tests.repositories.mysql_test_database import test_database
from tests.shops.mocks import shops_repository
from tests.sports.mocks import sports_repository
from tests.users.mocks import users_repository
from tests.equipments.mocks import equipments_repository


def configure(binder):
    binder.bind(Database, to=test_database)
    binder.bind(ClimatesRepository, to=climates_repository)
    binder.bind(RecommendationRepository, to=recommendations_repository)
    binder.bind(SportRepository, to=sports_repository)
    binder.bind(PracticeCentersRepository, to=practice_centers_repository)
    binder.bind(AnnouncesRepository, to=announces_repository)
    binder.bind(ShopsRepository, to=shops_repository)
    binder.bind(EquipmentRepository, to=equipments_repository)
    binder.bind(UsersRepository, to=users_repository)
