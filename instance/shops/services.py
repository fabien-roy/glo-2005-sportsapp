from injector import inject

from app.shops.repositories import ShopRepository
from instance.shops.fakes import shop1, shop2, shop3, shopN


class ShopPopulationService:
    @inject
    def __init__(self, shop_repository: ShopRepository):
        self.shop_repository = shop_repository

    def db_populate(self):
        self.shop_repository.add(shop1)
        self.shop_repository.add(shop2)
        self.shop_repository.add(shop3)
        # TODO : Remove
        for i in range(100):
            self.shop_repository.add(shopN)
