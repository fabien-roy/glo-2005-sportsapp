from injector import inject

from app.climates.models import Climate
from app.equipment_types.repositories import EquipmentTypeRepository
from app.sports.models import Sport
from app.sports.repositories import SportRepository
from instance.resources.helpers import read_elements, sports_csv


class SportPopulationService:
    @inject
    def __init__(self, sport_repository: SportRepository,
                 equipment_type_repository: EquipmentTypeRepository):
        self.sport_repository = sport_repository
        self.equipment_type_repository = equipment_type_repository

    def db_populate(self):
        for sport in self.read_sports():
            self.sport_repository.add(sport)

    def read_sports(self):
        return read_elements(sports_csv(), self.build_sport)

    def build_sport(self, row):
        climate = Climate(row[0])
        equipment_type = self.equipment_type_repository.get_by_name(row[2])
        return Sport(sport_id=None, name=row[1], climates=[climate],
                     required_equipment_types=[equipment_type])
