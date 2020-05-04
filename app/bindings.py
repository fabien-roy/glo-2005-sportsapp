from app.admin.modules import AdminModule
from app.announces.modules import AnnounceModule
from app.equipment_types.modules import EquipmentTypeModule
from app.climates.modules import ClimateModule
from app.equipments.modules import EquipmentModule
from app.interfaces.database import Database
from app.interfaces.infrastructure.database import MySQLDatabase
from app.manufacturers.modules import ManufacturerModule
from app.practice_centers.modules import PracticeCenterModule
from app.recommendations.modules import RecommendationModule
from app.shops.modules import ShopModule
from app.sports.modules import SportModule
from app.users.modules import UserModule


def configure_database(binder):
    binder.bind(Database, to=MySQLDatabase)


def configure_modules(binder):
    binder.install(AdminModule)
    binder.install(UserModule)
    binder.install(ClimateModule)
    binder.install(ShopModule)
    binder.install(ManufacturerModule)
    binder.install(EquipmentTypeModule)
    binder.install(EquipmentModule)
    binder.install(AnnounceModule)
    binder.install(SportModule)
    binder.install(PracticeCenterModule)
    binder.install(RecommendationModule)
