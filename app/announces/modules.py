from injector import Module

from app.announces.infrastructure.repositories import MySQLAnnounceRepository
from app.announces.repositories import AnnounceRepository


class AnnounceModule(Module):
    def configure(self, binder):
        binder.bind(AnnounceRepository, to=MySQLAnnounceRepository)
