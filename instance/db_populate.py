from app.climates.models import Climate
from app.practice_centers.models import PracticeCenter
from app.repositories.mysql_climate_repositories import MySQLClimateRepository
from app.repositories.mysql_user_repositories import MySQLUserRepository
from app.sports.models import Sport
from app.repositories.mysql_sport_repositories import MySQLSportRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCenterRepository


# TODO : Solve repository injection in db_populate.py
from app.users.models import User

sport_repository = MySQLSportRepository()
practice_center_repository = MySQLPracticeCenterRepository()
climate_repository = MySQLClimateRepository()
user_repository = MySQLUserRepository()


def db_populate():
    print('Populating database tables for SportsApp...')

    climate1 = Climate('tundra')
    climate2 = Climate('savane')
    climate3 = Climate('aride')
    climate_repository.add(climate1)
    climate_repository.add(climate2)
    climate_repository.add(climate3)

    sport1 = Sport(1, name='Randonnee', climates=[climate1, climate2])
    sport2 = Sport(2, name='Escalade', climates=[climate2, climate3])
    sport3 = Sport(3, name='Natation', climates=[climate3])
    sport_repository.add(sport1)
    sport_repository.add(sport2)
    sport_repository.add(sport3)

    center1 = PracticeCenter(1,
                             name='Mont-Orford National Park',
                             email='parc.mont-orford@sepaq.com',
                             web_site='https://www.sepaq.com/pq/mor/',
                             phone_number='819 843-9855',
                             climates=[climate2])
    center2 = PracticeCenter(2,
                             name='Parc des Montagnards',
                             email='info@censhefford.ca',
                             web_site='https://www.cantonsdelest.com/quoi-faire/980/parc-des-montagnards',
                             climates=[])
    center3 = PracticeCenter(3,
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

    print('...done!')
