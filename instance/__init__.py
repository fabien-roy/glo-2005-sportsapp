from injector import Injector

from app.announces.modules import AnnounceModule
from app.climates.modules import ClimateModule
from app.equipments.modules import EquipmentModule
from app.interfaces.database import Database
from app.practice_centers.modules import PracticeCenterModule
from app.recommendations.modules import RecommendationModule
from app.shops.modules import ShopModule
from app.sports.modules import SportModule
from app.users.modules import UserModule
from instance.creation.services import CreationService
from instance.population.services import PopulationService

injector = Injector([
    ClimateModule,
    SportModule,
    PracticeCenterModule,
    RecommendationModule,
    UserModule,
    AnnounceModule,
    ShopModule,
    EquipmentModule
])


class Instance:
    def __init__(self, database, instance_module):
        injector.binder.bind(Database, database)
        injector.binder.install(instance_module)

    @staticmethod
    def db_create():
        creation_service = injector.get(CreationService)
        creation_service.db_create()

    @staticmethod
    def db_populate():
        population_service = injector.get(PopulationService)
        population_service.db_populate()
