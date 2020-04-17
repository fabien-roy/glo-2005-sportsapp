from injector import inject

from app.practice_centers.repositories import PracticeCenterRepository
from instance.practice_centers.fakes import center1, center2, center3


class PracticeCenterPopulationService:
    @inject
    def __init__(self, practice_center_repository: PracticeCenterRepository):
        self.practice_center_repository = practice_center_repository

    def db_populate(self):
        self.practice_center_repository.add(center1)
        self.practice_center_repository.add(center2)
        self.practice_center_repository.add(center3)
