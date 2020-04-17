import inject

from app.sports.repositories import SportRepository
from instance.sports.fakes import sport1, sport2, sport3
from instance.sports.services import SportPopulationService


class MySQLSportPopulationService(SportPopulationService):
    sport_repository = inject.attr(SportRepository)

    def db_populate(self):
        self.sport_repository.add(sport1)
        self.sport_repository.add(sport2)
        self.sport_repository.add(sport3)
