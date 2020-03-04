import sys
import os

print('Creating database tables for SportsApp...')

if os.path.abspath(os.curdir) not in sys.path:
    print('...missing directory in PYTHONPATH... added!')
    sys.path.append(os.path.abspath(os.curdir))

from project import db
from project.models import User, Sport, PracticeCenter

db.drop_all()

db.create_all()

user1 = User(email='fabienroy28@gmail.com', plaintext_password='12341234', role='user')
user2 = User(email='test123@hotmail.ca', plaintext_password='password', role='user')
db.session.add(user1)
db.session.add(user2)

db.session.commit()

sport1 = Sport(name='Randonnée')
sport2 = Sport(name='Escalade')
sport3 = Sport(name='Natation')
db.session.add(sport1)
db.session.add(sport2)
db.session.add(sport3)

db.session.commit()

center1 = PracticeCenter(name='Mont-Orford National Park',
                         address='3321 Chemin du Parc, Orford, QC J1X 7A2',
                         email='parc.mont-orford@sepaq.com',
                         web_site='https://www.sepaq.com/pq/mor/',
                         phone_number='819 843-9855')
center2 = PracticeCenter(name='Parc des Montagnards',
                         address='333 Chemin du Mont-Shefford, Shefford, QC J2M 1N7',
                         email='info@censhefford.ca',
                         web_site='https://www.cantonsdelest.com/quoi-faire/980/parc-des-montagnards')
center3 = PracticeCenter(name='Gault Nature Reserve of McGill University',
                         address='422 Chemin des Moulins, Mont-Saint-Hilaire, QC J3G 4S6')
db.session.add(center1)
db.session.add(center2)
db.session.add(center3)

db.session.commit()

print('...done!')
