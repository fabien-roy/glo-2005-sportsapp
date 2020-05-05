from injector import inject

from app.climates.models import Climate
from app.practice_centers.models import PracticeCenter
from app.practice_centers.repositories import PracticeCenterRepository
from instance.resources.helpers import practice_centers_csv, read_elements


class PracticeCenterPopulationService:
    @inject
    def __init__(self, practice_center_repository: PracticeCenterRepository):
        self.practice_center_repository = practice_center_repository

    def db_populate(self):
        for practice_center in self.read_practice_centers():
            self.practice_center_repository.add(practice_center)

    def read_practice_centers(self):
        return read_elements(practice_centers_csv(), self.build_practice_center)

    @staticmethod
    def build_practice_center(row):
        climate = Climate(row[0])
        return PracticeCenter(practice_center_id=None, name=row[1], email=row[2], web_site=row[3],
                              phone_number=row[4], climates=[climate])
