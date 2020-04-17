from injector import inject

from app.sports.repositories import SportRepository
from instance.sports.fakes import sport1, sport2, sport3


class SportPopulationService:
    @inject
    def __init__(self, sport_repository: SportRepository):
        self.sport_repository = sport_repository

    def db_populate(self):
        self.sport_repository.add(sport1)
        self.sport_repository.add(sport2)
        self.sport_repository.add(sport3)
