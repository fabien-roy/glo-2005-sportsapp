from app.climates.models import Climate
from app.practice_centers.models import PracticeCenter
from app.recommendations.models import Recommendation
from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_user_repositories import MySQLUsersRepository
from app.sports.models import Sport
from app.repositories.mysql_sport_repositories import MySQLSportsRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCentersRepository
from app.users.models import User
from app.shops.models import Shop
from app.repositories.mysql_shop_repositories import MySQLShopsRepository

# TODO : Solve repository injection in db_populate.py
sport_repository = MySQLSportsRepository()
practice_center_repository = MySQLPracticeCentersRepository()
climate_repository = MySQLClimatesRepository()
recommendation_repository = MySQLRecommendationsRepository()
user_repository = MySQLUsersRepository()
shop_repository = MySQLShopsRepository()


def db_populate():
    print('Populating database tables for SportsApp...')

    climate1 = Climate('tundra')
    climate2 = Climate('savane')
    climate3 = Climate('aride')
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
    sport_repository.add_recommendation(sport1.id, sport1_recommendation1)
    sport_repository.add_recommendation(sport2.id, sport2_recommendation1)
    sport_repository.add_recommendation(sport2.id, sport2_recommendation2)
    sport_repository.add_recommendation(sport3.id, sport3_recommendation1)

    center1_recommendation1 = Recommendation(None, center1.id, user1.username, 'Un super centre. J\' adore.', 5,
                                             center1.name)
    center2_recommendation1 = Recommendation(None, center2.id, user1.username, 'Cool.', 3, center2.name)
    center2_recommendation2 = Recommendation(None, center2.id, user2.username, 'Pourri, mais bon, 2 étoiles.', 2,
                                             center2.name)
    center3_recommendation1 = Recommendation(None, center3.id, user3.username, ':D', 0, center3.name)
    center3_recommendation2 = Recommendation(None, center3.id, user1.username, 'Noice.', 4, center3.name)
    practice_center_repository.add_recommendation(center1.id, center1_recommendation1)
    practice_center_repository.add_recommendation(center2.id, center2_recommendation1)
    practice_center_repository.add_recommendation(center2.id, center2_recommendation2)
    practice_center_repository.add_recommendation(center3.id, center3_recommendation1)
    practice_center_repository.add_recommendation(center3.id, center3_recommendation2)

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


    print('...done!')
