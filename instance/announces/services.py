from injector import inject

from app.announces.repositories import AnnounceRepository
from instance.announces.fakes import shop1_equipment2_announce1, shop2_equipment2_announce1, \
    shop1_equipment1_announce1, shop2_equipment2_announce2, shop3_equipment1_announce1, \
    shop3_equipment3_announce1
from instance.equipments.fakes import equipment1, equipment3, equipment2
from instance.shops.fakes import shop1, shop2, shop3


class AnnouncePopulationService:
    @inject
    def __init__(self, announce_repository: AnnounceRepository):
        self.announce_repository = announce_repository

    def db_populate(self):
        self.announce_repository.add(shop1_equipment1_announce1, shop1.id, equipment1.id)
        self.announce_repository.add(shop1_equipment2_announce1, shop1.id, equipment2.id)
        self.announce_repository.add(shop2_equipment2_announce1, shop2.id, equipment2.id)
        self.announce_repository.add(shop2_equipment2_announce2, shop2.id, equipment2.id)
        self.announce_repository.add(shop3_equipment1_announce1, shop3.id, equipment1.id)
        self.announce_repository.add(shop3_equipment3_announce1, shop3.id, equipment3.id)
