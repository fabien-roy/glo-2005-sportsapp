from injector import inject

from app.climates.repositories import ClimateRepository
from instance.climates.fakes import climate1, climate2, climate3


class ClimatePopulationService:
    @inject
    def __init__(self, climate_repository: ClimateRepository):
        self.climate_repository = climate_repository

    def db_populate(self):
        self.climate_repository.add(climate1)
        self.climate_repository.add(climate2)
        self.climate_repository.add(climate3)
