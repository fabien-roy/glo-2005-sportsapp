from app.shops.repositories import ShopRepository
from instance import injector
from instance.shops.fakes import shop1, shop2, shop3

shop_repository = injector.get(ShopRepository)


def db_populate_with_shops():
    shop_repository.add(shop1)
    shop_repository.add(shop2)
    shop_repository.add(shop3)
