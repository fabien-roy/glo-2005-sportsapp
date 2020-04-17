import inject

from app.practice_centers.repositories import PracticeCenterRepository
from instance.practice_centers.fakes import center1, center2, center3
from instance.practice_centers.services import PracticeCenterPopulationService


class MySQLPracticeCenterPopulationService(PracticeCenterPopulationService):
    practice_center_repository = inject.attr(PracticeCenterRepository)

    def db_populate(self):
        self.practice_center_repository.add(center1)
        self.practice_center_repository.add(center2)
        self.practice_center_repository.add(center3)
