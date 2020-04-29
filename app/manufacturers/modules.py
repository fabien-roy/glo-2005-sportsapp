from injector import Module

from app.manufacturers.infrastructure.repositories import MySQLManufacturerRepository
from app.manufacturers.repositories import ManufacturerRepository


class ManufacturerModule(Module):
    def configure(self, binder):
        binder.bind(ManufacturerRepository, to=MySQLManufacturerRepository)
