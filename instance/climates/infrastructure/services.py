import inject

from app.climates.repositories import ClimateRepository
from instance.climates.fakes import climate1, climate2, climate3
from instance.climates.services import ClimatePopulationService


class MySQLClimatePopulationService(ClimatePopulationService):
    climate_repository = inject.attr(ClimateRepository)

    def db_populate(self):
        self.climate_repository.add(climate1)
        self.climate_repository.add(climate2)
        self.climate_repository.add(climate3)
