from app.sports.repositories import SportRepository
from instance import injector
from instance.sports.fakes import sport1, sport2, sport3

sport_repository = injector.get(SportRepository)


def db_populate_with_sports():
    sport_repository.add(sport1)
    sport_repository.add(sport2)
    sport_repository.add(sport3)
