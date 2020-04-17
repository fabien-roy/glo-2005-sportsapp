from injector import Injector

injector = Injector()

from instance.creation.services import CreationService
from instance.population.services import PopulationService


def db_create():
    creation_service = injector.get(CreationService)
    creation_service.db_create()


def db_populate():
    population_service = injector.get(PopulationService)
    population_service.db_populate()
