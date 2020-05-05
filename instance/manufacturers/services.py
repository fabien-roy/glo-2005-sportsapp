from injector import inject

from app.manufacturers.models import Manufacturer
from app.manufacturers.repositories import ManufacturerRepository
from instance.resources.helpers import read_elements, manufacturers_csv


class ManufacturerPopulationService:
    @inject
    def __init__(self, manufacturer_repository: ManufacturerRepository):
        self.manufacturer_repository = manufacturer_repository

    def db_populate(self):
        for manufacturer in self.read_manufacturers():
            self.manufacturer_repository.add(manufacturer)

    def read_manufacturers(self):
        return read_elements(manufacturers_csv(), self.build_manufacturer)

    @staticmethod
    def build_manufacturer(row):
        return Manufacturer(manufacturer_id=None, name=row[0])
