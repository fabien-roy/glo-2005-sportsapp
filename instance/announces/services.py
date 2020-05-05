from injector import inject

from app.announces.models import Announce
from app.announces.repositories import AnnounceRepository
from app.equipments.repositories import EquipmentRepository
from app.shops.repositories import ShopRepository
from instance.resources.helpers import read_elements, announces_csv


class AnnouncePopulationService:
    @inject
    def __init__(self, announce_repository: AnnounceRepository, shop_repository: ShopRepository,
                 equipment_repository: EquipmentRepository):
        self.announce_repository = announce_repository
        self.shop_repository = shop_repository
        self.equipment_repository = equipment_repository

    def db_populate(self):
        for announce, shop_id, equipment_id in self.read_announces():
            self.announce_repository.add(announce, shop_id, equipment_id)

    def read_announces(self):
        return read_elements(announces_csv(), self.build_announce)

    def build_announce(self, row):
        shop = self.shop_repository.get_by_name(row[0])
        equipment = self.equipment_repository.get_by_name(row[1])
        return Announce(announce_id=None, shop_id=None, shop_name=None, equipment_id=None,
                        equipment_name=None, state=row[2], price=row[3]), shop.id, equipment.id
