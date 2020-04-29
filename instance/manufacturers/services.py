from injector import inject

from app.manufacturers.repositories import ManufacturerRepository
from instance.manufacturers.fakes import manufacturer1, manufacturer2, manufacturer3


class ManufacturerPopulationService:
    @inject
    def __init__(self, manufacturer_repository: ManufacturerRepository):
        self.manufacturer_repository = manufacturer_repository

    def db_populate(self):
        self.manufacturer_repository.add(manufacturer1)
        self.manufacturer_repository.add(manufacturer2)
        self.manufacturer_repository.add(manufacturer3)
