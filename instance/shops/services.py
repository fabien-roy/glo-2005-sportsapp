from injector import inject

from app.shops.models import Shop
from app.shops.repositories import ShopRepository
from instance.resources.helpers import read_elements, shops_csv


class ShopPopulationService:
    @inject
    def __init__(self, shop_repository: ShopRepository):
        self.shop_repository = shop_repository

    def db_populate(self):
        for shop in self.read_shops():
            self.shop_repository.add(shop)

    def read_shops(self):
        return read_elements(shops_csv(), self.build_shop)

    @staticmethod
    def build_shop(row):
        return Shop(shop_id=None, name=row[0], email=row[1], web_site=row[2], phone_number=row[3])
