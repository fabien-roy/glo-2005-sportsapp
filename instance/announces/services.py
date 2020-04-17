from app.announces.repositories import AnnounceRepository
from instance import injector
from instance.announces.fakes import announce2, announce3, announce1, announce4, announce5, \
    announce6

announce_repository = injector.get(AnnounceRepository)


def db_populate_with_announces():
    announce_repository.add(announce1)
    announce_repository.add(announce2)
    announce_repository.add(announce3)
    announce_repository.add(announce4)
    announce_repository.add(announce5)
    announce_repository.add(announce6)
