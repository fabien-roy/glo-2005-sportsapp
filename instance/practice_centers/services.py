from app.practice_centers.repositories import PracticeCenterRepository
from instance import injector
from instance.practice_centers.fakes import center1, center2, center3

practice_center_repository = injector.get(PracticeCenterRepository)


def db_populate_practice_centers():
    practice_center_repository.add(center1)
    practice_center_repository.add(center2)
    practice_center_repository.add(center3)
