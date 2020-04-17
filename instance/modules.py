from injector import Module

from instance import CreationService, PopulationService
from instance.creation.infrastructure.services import MySQLCreationService
from instance.population.infrastructure.services import MySQLPopulationService


class InstanceModule(Module):
    def configure(self, binder):
        binder.bind(CreationService, to=MySQLCreationService)
        binder.bind(PopulationService, to=MySQLPopulationService)
