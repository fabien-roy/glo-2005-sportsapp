from injector import inject

from app.climates.models import Climate
from app.equipment_types.models import EquipmentType
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
        climate = Climate(row[0])
        equipment_type = EquipmentType(type_id=None, name=row[2])
        return Sport(sport_id=None, name=row[1], climates=[climate],
                     required_equipment_types=[equipment_type])
