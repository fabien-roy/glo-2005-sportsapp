from injector import Module

from app.practice_centers.infrastructure.repositories import MySQLPracticeCenterRepository
from app.practice_centers.repositories import PracticeCenterRepository


class PracticeCenterModule(Module):
    def configure(self, binder):
        binder.bind(PracticeCenterRepository, to=MySQLPracticeCenterRepository)
