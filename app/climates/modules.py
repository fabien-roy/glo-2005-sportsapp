from injector import Module

from app.climates.infrastructure.repositories import MySQLClimateRepository
from app.climates.repositories import ClimateRepository


class ClimateModule(Module):
    def configure(self, binder):
        binder.bind(ClimateRepository, to=MySQLClimateRepository)
