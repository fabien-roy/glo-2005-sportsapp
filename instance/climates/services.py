from injector import inject

from app.climates.models import Climate
from app.climates.repositories import ClimateRepository
from instance.resources.helpers import read_elements, climates_csv


class ClimatePopulationService:
    @inject
    def __init__(self, climate_repository: ClimateRepository):
        self.climate_repository = climate_repository

    def db_populate(self):
        for climate in self.read_climates():
            self.climate_repository.add(climate)

    def read_climates(self):
        return read_elements(climates_csv(), self.build_climate)

    @staticmethod
    def build_climate(row):
        return Climate(name=row[0])
