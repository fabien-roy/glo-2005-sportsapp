from injector import Module

from app.shops.infrastructure.repositories import MySQLShopRepository
from app.shops.repositories import ShopRepository


class ShopModule(Module):
    def configure(self, binder):
        binder.bind(ShopRepository, to=MySQLShopRepository)
