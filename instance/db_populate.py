from app.climates.models import Climate
from app.practice_centers.models import PracticeCenter
from app.recommendations.models import Recommendation
from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_database import MySQLDatabase
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.sports.models import Sport
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.users.models import User
from app.shops.models import Shop
from app.repositories.mysql_shop_repositories import MySQLShopsRepository
from app.equipments.models import Equipment
from app.repositories.mysql_equipment_repositories import MySQLEquipmentsRepository

database = MySQLDatabase()
climate_repository = MySQLClimatesRepository(database)
recommendation_repository = MySQLRecommendationsRepository(database)
sport_repository = MySQLSportsRepository(database, climate_repository, recommendation_repository)
practice_center_repository = MySQLPracticeCentersRepository(database, climate_repository,
                                                            recommendation_repository)
user_repository = MySQLUsersRepository(database, recommendation_repository)
shop_repository = MySQLShopsRepository(database)
equipment_repository = MySQLEquipmentsRepository(database)


def db_populate():
    print('Populating database tables for SportsApp...')

    climate1 = Climate('Tundra')
    climate2 = Climate('Savane')
    climate3 = Climate('Aride')
    climate_repository.add(climate1)
    climate_repository.add(climate2)
    climate_repository.add(climate3)

    sport1 = Sport(None, name='Randonnee', climates=[climate1, climate2])
    sport2 = Sport(None, name='Escalade', climates=[climate2, climate3])
    sport3 = Sport(None, name='Natation', climates=[climate3])
    sport_repository.add(sport1)
    sport_repository.add(sport2)
    sport_repository.add(sport3)

    center1 = PracticeCenter(None,
                             name='Mont-Orford National Park',
                             email='parc.mont-orford@sepaq.com',
                             web_site='https://www.sepaq.com/pq/mor/',
                             phone_number='819 843-9855',
                             climates=[climate2])
    center2 = PracticeCenter(None,
                             name='Parc des Montagnards',
                             email='info@censhefford.ca',
                             web_site='https://www.cantonsdelest.com/quoi-faire/980/parc-des-montagnards',
                             climates=[])
    center3 = PracticeCenter(None,
                             name='Gault Nature Reserve of McGill University',
                             climates=[climate1, climate3])
    practice_center_repository.add(center1)
    practice_center_repository.add(center2)
    practice_center_repository.add(center3)

    user1 = User(username='fabienroy28', email='fabienroy28@gmail.com', first_name='Fabien', last_name='Roy',
                 phone_number='123-456-7890')
    user2 = User(username='mikaelvalliant', email='mikaelvalliant@gmail.com', first_name='Mikael', last_name='Valliant')
    user3 = User(username='getoutmyswamp', email='shrek@swamp.ca', first_name='Shrek', phone_number='1 800-555-0101')
    user_repository.add(user1)
    user_repository.add(user2)
    user_repository.add(user3)

    sport1_recommendation1 = Recommendation(None, sport1.id, user1.username, 'Un super sport. J\' adore.', 5,
                                            sport1.name)
    sport2_recommendation1 = Recommendation(None, sport2.id, user3.username, 'Cool.', 3, sport2.name)
    sport2_recommendation2 = Recommendation(None, sport2.id, user2.username, 'Pourri.', 0, sport2.name)
    sport3_recommendation1 = Recommendation(None, sport3.id, user1.username, ':D', 5, sport3.name)
    recommendation_repository.add_for_sport(sport1_recommendation1, sport1)
    recommendation_repository.add_for_sport(sport2_recommendation1, sport2)
    recommendation_repository.add_for_sport(sport2_recommendation2, sport2)
    recommendation_repository.add_for_sport(sport3_recommendation1, sport3)

    center1_recommendation1 = Recommendation(None, center1.id, user1.username, 'Un super centre. J\' adore.', 5,
                                             center1.name)
    center2_recommendation1 = Recommendation(None, center2.id, user1.username, 'Cool.', 3, center2.name)
    center2_recommendation2 = Recommendation(None, center2.id, user2.username, 'Pourri, mais bon, 2 étoiles.', 2,
                                             center2.name)
    center3_recommendation1 = Recommendation(None, center3.id, user3.username, ':D', 0, center3.name)
    center3_recommendation2 = Recommendation(None, center3.id, user1.username, 'Noice.', 4, center3.name)
    recommendation_repository.add_for_practice_center(center1_recommendation1, center1)
    recommendation_repository.add_for_practice_center(center2_recommendation1, center2)
    recommendation_repository.add_for_practice_center(center2_recommendation2, center2)
    recommendation_repository.add_for_practice_center(center3_recommendation1, center3)
    recommendation_repository.add_for_practice_center(center3_recommendation2, center3)

    shop1 = Shop(None, name='MEC Quebec City', phone_number='418 522-8884',
                 web_site='https://www.mec.ca/fr/stores/quebec?utm_medium=organic&utm'
                          'source=google&utm_campaign=my-business-listings&utm_content=quebec')
    shop2 = Shop(None, name='Sportium', phone_number='418 627-0073',
                 web_site='https://www.sportium.ca/fr/nos-magasins/quebec')
    shop3 = Shop(None, name='Au Grand Bazar La Source Du Sport', phone_number='450 378-2022',
                 email='info@grandbazar.ca',
                 web_site='https://grandbazar.ca/fr/')
    shop_repository.add(shop1)
    shop_repository.add(shop2)
    shop_repository.add(shop3)

    equipment1 = Equipment(None, category='hiking', name="Men’s Wayfinder™ Mid OutDry™ Boot", description="Our "
                                                                                                          "signature waterproof construction keeps this multisport shoe comfortably dry for "
                                                                                                          "any activity—in any weather.")
    equipment2 = Equipment(None, category='running', name="Men's F.K.T.™ Lite Trail Running Shoe",
                           description="This lightweight trail runner lets you reach your "
                                       "fastest time without sacrificing performance.")
    equipment3 = Equipment(None, category='recovery', name="Men's Molokai™ III Recovery Sandal",
                           description="After a tough trail run there’s nothing more soothing for your feet than the "
                                       "men’s Molokai III Recovery Sandal. Crafted with a supportive midsole and a "
                                       "moldable footbed to fit even the most tortured feet.")
    equipment_repository.add(equipment1)
    equipment_repository.add(equipment2)
    equipment_repository.add(equipment3)

    print('...done!')
