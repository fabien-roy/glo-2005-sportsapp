from injector import inject

from instance.climates.services import ClimatePopulationService
from instance.manufacturers.services import ManufacturerPopulationService
from instance.sports.services import SportPopulationService
from instance.practice_centers.services import PracticeCenterPopulationService
from instance.users.services import UserPopulationService
from instance.recommendations.services import RecommendationPopulationService
from instance.shops.services import ShopPopulationService
from instance.equipments.services import EquipmentPopulationService
from instance.announces.services import AnnouncePopulationService


class PopulationService:
    @inject
    def __init__(self,
                 climate_population_service: ClimatePopulationService,
                 sport_population_service: SportPopulationService,
                 practice_center_population_service: PracticeCenterPopulationService,
                 user_population_service: UserPopulationService,
                 recommendation_population_service: RecommendationPopulationService,
                 shop_population_service: ShopPopulationService,
                 manufacturer_population_service: ManufacturerPopulationService,
                 equipment_population_service: EquipmentPopulationService,
                 announce_population_service: AnnouncePopulationService):
        self.climate_population_service = climate_population_service
        self.sport_population_service = sport_population_service
        self.practice_center_population_service = practice_center_population_service
        self.user_population_service = user_population_service
        self.recommendation_population_service = recommendation_population_service
        self.shop_population_service = shop_population_service
        self.manufacturer_population_service = manufacturer_population_service
        self.equipment_population_service = equipment_population_service
        self.announce_population_service = announce_population_service

    def db_populate(self):
        print('Populating database tables for SportsApp...')

        self.climate_population_service.db_populate()
        self.sport_population_service.db_populate()
        self.practice_center_population_service.db_populate()
        self.user_population_service.db_populate()
        self.recommendation_population_service.db_populate()
        self.shop_population_service.db_populate()
        self.manufacturer_population_service.db_populate()
        self.equipment_population_service.db_populate()
        self.announce_population_service.db_populate()

        print('...done!')
