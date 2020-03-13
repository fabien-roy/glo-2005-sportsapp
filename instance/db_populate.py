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

# TODO : Solve repository injection in db_populate.py
sport_repository = MySQLSportsRepository()
practice_center_repository = MySQLPracticeCentersRepository()
climate_repository = MySQLClimatesRepository()
recommendation_repository = MySQLRecommendationsRepository()
user_repository = MySQLUsersRepository()


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

    sport1_recommendation1 = Recommendation(None, username=user1.username, comment='Un super sport. J\' adore.', note=5)
    sport2_recommendation1 = Recommendation(None, username=user3.username, comment='Cool.', note=3)
    sport2_recommendation2 = Recommendation(None, username=user2.username, comment='Pourri.', note=0)
    sport3_recommendation1 = Recommendation(None, username=user1.username, comment=':D', note=5)
    sport_repository.add_recommendation(sport1.id, sport1_recommendation1)
    sport_repository.add_recommendation(sport2.id, sport2_recommendation1)
    sport_repository.add_recommendation(sport2.id, sport2_recommendation2)
    sport_repository.add_recommendation(sport3.id, sport3_recommendation1)

    center1_recommendation1 = Recommendation(None, username=user1.username, comment='Un super centre. J\' adore.', note=5)
    center2_recommendation1 = Recommendation(None, username=user1.username, comment='Cool.', note=3)
    center2_recommendation2 = Recommendation(None, username=user2.username, comment='Pourri, mais bon, 2 étoiles.', note=2)
    center3_recommendation1 = Recommendation(None, username=user3.username, comment=':D', note=0)
    center3_recommendation2 = Recommendation(None, username=user1.username, comment='Noice.', note=4)
    practice_center_repository.add_recommendation(center1.id, center1_recommendation1)
    practice_center_repository.add_recommendation(center2.id, center2_recommendation1)
    practice_center_repository.add_recommendation(center2.id, center2_recommendation2)
    practice_center_repository.add_recommendation(center3.id, center3_recommendation1)
    practice_center_repository.add_recommendation(center3.id, center3_recommendation2)

    print('...done!')
