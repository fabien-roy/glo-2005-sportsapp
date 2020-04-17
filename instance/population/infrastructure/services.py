import inject

from app.announces.models import Announce
from app.equipments.models import Equipment
from app.practice_centers.models import PracticeCenter
from app.recommendations.models import Recommendation
from app.shops.models import Shop
from app.users.models import User
from instance.climates.fakes import climate1
from instance.climates.services import ClimatePopulationService
from instance.practice_centers.services import PracticeCenterPopulationService
from instance.sports.services import SportPopulationService
from instance.users.services import UserPopulationService


class MySQLPopulationService:
    climate_population_service = inject.attr(ClimatePopulationService)
    sport_population_service = inject.attr(SportPopulationService)
    practice_population_service = inject.attr(PracticeCenterPopulationService)
    user_population_service = inject.attr(UserPopulationService)
    recommendation_repository = inject.attr(recommendation_repository)
    announce_repository = inject.attr(announce_repository)
    shop_repository = inject.attr(shop_repository)
    equipment_repository = inject.attr(equipment_repository)

    def db_populate(self):
        print('Populating database tables for SportsApp...')

        self.climate_population_service.db_populate()
        self.sport_population_service.db_populate()
        self.practice_population_service.db_populate()
        self.user_population_service.db_populate()

        sport1_recommendation1 = Recommendation(None, sport1.id, user1.username,
                                                'Un super sport. J\' adore.', 5, sport1.name)
        sport2_recommendation1 = Recommendation(None, sport2.id, user3.username,
                                                'Cool.', 3, sport2.name)
        sport2_recommendation2 = Recommendation(None, sport2.id, user2.username,
                                                'Pourri.', 0, sport2.name)
        sport3_recommendation1 = Recommendation(None, sport3.id, user1.username,
                                                ':D', 5, sport3.name)
        self.recommendation_repository.add_for_sport(sport1_recommendation1, sport1)
        self.recommendation_repository.add_for_sport(sport2_recommendation1, sport2)
        self.recommendation_repository.add_for_sport(sport2_recommendation2, sport2)
        self.recommendation_repository.add_for_sport(sport3_recommendation1, sport3)

        center1_recommendation1 = Recommendation(None, center1.id, user1.username,
                                                 'Un super centre. J\' adore.', 5, center1.name)
        center2_recommendation1 = Recommendation(None, center2.id, user1.username,
                                                 'Cool.', 3, center2.name)
        center2_recommendation2 = Recommendation(None, center2.id, user2.username,
                                                 'Pourri, mais bon, 2 étoiles.', 2, center2.name)
        center3_recommendation1 = Recommendation(None, center3.id,
                                                 user3.username, ':D', 0, center3.name)
        center3_recommendation2 = Recommendation(None, center3.id,
                                                 user1.username, 'Noice.', 4, center3.name)
        self.recommendation_repository.add_for_practice_center(center1_recommendation1, center1)
        self.recommendation_repository.add_for_practice_center(center2_recommendation1, center2)
        self.recommendation_repository.add_for_practice_center(center2_recommendation2, center2)
        self.recommendation_repository.add_for_practice_center(center3_recommendation1, center3)
        self.recommendation_repository.add_for_practice_center(center3_recommendation2, center3)

        shop1 = Shop(None, name='MEC Quebec City', phone_number='418 522-8884',
                     web_site='https://www.mec.ca/fr/stores/quebec?utm_medium=organic&utm'
                              'source=google&utm_campaign=my-business-listings&utm_content=quebec')
        shop2 = Shop(None, name='Sportium', phone_number='418 627-0073',
                     web_site='https://www.sportium.ca/fr/nos-magasins/quebec')
        shop3 = Shop(None, name='Au Grand Bazar La Source Du Sport', phone_number='450 378-2022',
                     email='info@grandbazar.ca',
                     web_site='https://grandbazar.ca/fr/')
        self.shop_repository.add(shop1)
        self.shop_repository.add(shop2)
        self.shop_repository.add(shop3)

        equipment1 = Equipment(None, category='hiking', name="Men’s Wayfinder™ Mid OutDry™ Boot",
                               description="Our signature waterproof construction keeps "
                                           "this multisport shoe comfortably dry for "
                                           "any activity—in any weather.")
        equipment2 = Equipment(None, category='running',
                               name="Men's F.K.T.™ Lite Trail Running Shoe",
                               description="This lightweight trail runner lets you reach your "
                                           "fastest time without sacrificing performance.")
        equipment3 = Equipment(None, category='recovery', name="Men's Molokai™ III Recovery Sandal",
                               description="After a tough trail run there’s nothing more soothing for "
                                           "your feet than the men’s Molokai III Recovery "
                                           "Sandal. Crafted with a supportive midsole"
                                           " and a moldable footbed to fit even the"
                                           " most tortured feet.")
        self.equipment_repository.add(equipment1)
        self.equipment_repository.add(equipment2)
        self.equipment_repository.add(equipment3)

        announce1 = Announce(None, shop1.id, shop1.name, equipment1.id, equipment1.name, 'New',
                             199.99, )
        announce2 = Announce(None, shop1.id, shop1.name, equipment2.id, equipment2.name, 'Used',
                             149.99, )
        announce3 = Announce(None, shop2.id, shop2.name, equipment2.id, equipment2.name, 'New',
                             400.00, )
        announce4 = Announce(None, shop2.id, shop2.name, equipment2.id, equipment2.name,
                             'Needs repair',
                             300.00, )
        announce5 = Announce(None, shop3.id, shop3.name, equipment1.id, equipment1.name, 'Used',
                             49.99, )
        announce6 = Announce(None, shop3.id, shop3.name, equipment3.id, equipment3.name, 'Used',
                             99.99, )
        self.announce_repository.add(announce1)
        self.announce_repository.add(announce2)
        self.announce_repository.add(announce3)
        self.announce_repository.add(announce4)
        self.announce_repository.add(announce5)
        self.announce_repository.add(announce6)

        print('...done!')
