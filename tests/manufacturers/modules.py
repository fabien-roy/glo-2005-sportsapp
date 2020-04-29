from injector import Module

from app.manufacturers.repositories import ManufacturerRepository
from tests.manufacturers.mocks import manufacturer_repository


class MockManufacturerModule(Module):
    def configure(self, binder):
        binder.bind(ManufacturerRepository, to=manufacturer_repository)
