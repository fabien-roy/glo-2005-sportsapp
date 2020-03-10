from app.practice_centers.models import PracticeCenter
from app.sports.models import Sport
from app.repositories.mysql_sport_repositories import MySQLSportRepository
from app.repositories.mysql_practice_center_repositories import MySQLPracticeCenterRepository


# TODO : Solve repository injection in db_populate.py
sport_repository = MySQLSportRepository()
practice_center_repository = MySQLPracticeCenterRepository()


def db_populate():
    print('Populating database tables for SportsApp...')

    # TODO : Add users mocked data

    sport1 = Sport(None, name='Randonnee')
    sport2 = Sport(None, name='Escalade')
    sport3 = Sport(None, name='Natation')
    sport_repository.add(sport1)
    sport_repository.add(sport2)
    sport_repository.add(sport3)

    center1 = PracticeCenter(None,
                             name='Mont-Orford National Park',
                             email='parc.mont-orford@sepaq.com',
                             web_site='https://www.sepaq.com/pq/mor/',
                             phone_number='819 843-9855')
    center2 = PracticeCenter(None,
                             name='Parc des Montagnards',
                             email='info@censhefford.ca',
                             web_site='https://www.cantonsdelest.com/quoi-faire/980/parc-des-montagnards')
    center3 = PracticeCenter(None,
                             name='Gault Nature Reserve of McGill University')
    practice_center_repository.add(center1)
    practice_center_repository.add(center2)
    practice_center_repository.add(center3)

    print('...done!')
