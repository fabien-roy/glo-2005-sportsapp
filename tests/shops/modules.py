from injector import Module

from app.shops.repositories import ShopRepository
from tests.shops.mocks import shop_repository


class MockShopModule(Module):
    def configure(self, binder):
        binder.bind(ShopRepository, to=shop_repository)
