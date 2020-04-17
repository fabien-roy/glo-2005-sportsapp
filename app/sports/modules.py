from injector import Module

from app.sports.infrastructure.repositories import MySQLSportRepository
from app.sports.repositories import SportRepository


class SportModule(Module):
    def configure(self, binder):
        binder.bind(SportRepository, to=MySQLSportRepository)
