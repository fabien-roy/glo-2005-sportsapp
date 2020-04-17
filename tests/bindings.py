from app.interfaces.database import Database
from tests.announces.modules import MockAnnounceModule
from tests.climates.modules import MockClimateModule
from tests.equipments.modules import MockEquipmentModule
from tests.interfaces.infrastructure.database import test_database
from tests.practice_centers.modules import MockPracticeCenterModule
from tests.recommendations.modules import MockRecommendationModule
from tests.shops.modules import MockShopModule
from tests.sports.modules import MockSportModule
from tests.users.modules import MockUserModule


def configure(binder):
    binder.bind(Database, to=test_database)

    binder.install(MockClimateModule)
    binder.install(MockSportModule)
    binder.install(MockPracticeCenterModule)
    binder.install(MockRecommendationModule)
    binder.install(MockUserModule)
    binder.install(MockAnnounceModule)
    binder.install(MockShopModule)
    binder.install(MockEquipmentModule)
