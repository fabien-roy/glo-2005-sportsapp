from app.announces.modules import AnnounceModule
from app.climates.modules import ClimateModule
from app.equipments.modules import EquipmentModule
from app.interfaces.database import Database
from app.interfaces.infrastructure.database import MySQLDatabase
from app.practice_centers.modules import PracticeCenterModule
from app.recommendations.modules import RecommendationModule
from app.shops.modules import ShopModule
from app.sports.modules import SportModule
from app.users.modules import UserModule


def configure_database(binder):
    binder.bind(Database, to=MySQLDatabase)


def configure_modules(binder):
    binder.install(ClimateModule)
    binder.install(SportModule)
    binder.install(PracticeCenterModule)
    binder.install(RecommendationModule)
    binder.install(UserModule)
    binder.install(AnnounceModule)
    binder.install(ShopModule)
    binder.install(EquipmentModule)
