from injector import inject

from app.climates.models import Climate
from app.sports.models import Sport
from app.sports.repositories import SportRepository
from instance.resources.helpers import read_elements, sports_csv


class SportPopulationService:
    @inject
    def __init__(self, sport_repository: SportRepository):
        self.sport_repository = sport_repository

    def db_populate(self):
        for sport in self.read_sports():
            self.sport_repository.add(sport)

    def read_sports(self):
        return read_elements(sports_csv(), self.build_sport)

    @staticmethod
    def build_sport(row):
        return Sport(sport_id=None, name=row[1], climates=[Climate(row[0])])
