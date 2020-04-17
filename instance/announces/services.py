from injector import inject

from app.announces.repositories import AnnounceRepository
from instance.announces.fakes import announce2, announce3, announce1, announce4, announce5, \
    announce6


class AnnouncePopulationService:
    @inject
    def __init__(self, announce_repository: AnnounceRepository):
        self.announce_repository = announce_repository

    def db_populate(self):
        self.announce_repository.add(announce1)
        self.announce_repository.add(announce2)
        self.announce_repository.add(announce3)
        self.announce_repository.add(announce4)
        self.announce_repository.add(announce5)
        self.announce_repository.add(announce6)
