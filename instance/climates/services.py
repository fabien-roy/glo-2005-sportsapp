from app.climates.repositories import ClimateRepository
from instance import injector
from instance.climates.fakes import climate1, climate2, climate3

climate_repository = injector.get(ClimateRepository)


def db_populate_with_climates():
    climate_repository.add(climate1)
    climate_repository.add(climate2)
    climate_repository.add(climate3)
