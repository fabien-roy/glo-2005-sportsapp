from app.climates.models import Climate
from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.models import PracticeCenter
from app.recommendations.models import Recommendation
from app.sports.models import Sport
from app.sports.exceptions import SportNotFoundException

# Climates
from app.users.exceptions import UserNotFoundException
from app.users.models import User

climate1 = Climate('tundra')
climate2 = Climate('savane')
climate3 = Climate('aride')

# Sports

sport1 = Sport(sport_id=1, name='Randonnee', climates=[climate1, climate2])
sport2 = Sport(sport_id=2, name='Escalade', climates=[climate2, climate3])
sport3 = Sport(sport_id=3, name='Natation', climates=[climate3])


def sports(sport_id):
    return {
        '1': sport1,
        '2': sport2,
        '3': sport3
    }[sport_id]


def no_sport():
    raise SportNotFoundException


# Practice Centers

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


def practice_centers(practice_center_id):
    return {
        '1': center1,
        '2': center2,
        '3': center3
    }[practice_center_id]


def no_practice_center():
    raise PracticeCenterNotFoundException


# Users

user1 = User(username='fabienroy28', email='fabienroy28@gmail.com', first_name='Fabien', last_name='Roy',
             phone_number='123-456-7890')
user2 = User(username='mikaelvalliant', email='mikaelvalliant@gmail.com', first_name='Mikael', last_name='Valliant')
user3 = User(username='getoutmyswamp', email='shrek@swamp.ca', first_name='Shrek', phone_number='1 800-555-0101')


def users(username):
    return {
        'fabienroy28': user1,
        'mikaelvalliant': user2,
        'getoutmyswamp': user3
    }[username]


def no_user():
    raise UserNotFoundException

# Recommendations

sport1_recommendation1 = Recommendation(1, username=user1.username, comment='Un super sport. J\' adore.', note=5)
sport2_recommendation1 = Recommendation(2, username=user3.username, comment='Cool.', note=3)
sport2_recommendation2 = Recommendation(3, username=user2.username, comment='Pourri.', note=0)
sport3_recommendation1 = Recommendation(4, username=user1.username, comment=':D', note=5)
sport1.add_recommendation(sport1_recommendation1)
sport2.add_recommendation(sport2_recommendation1)
sport2.add_recommendation(sport2_recommendation2)
sport3.add_recommendation(sport3_recommendation1)

center1_recommendation1 = Recommendation(None, username=user1.username, comment='Un super centre. J\' adore.', note=5)
center2_recommendation1 = Recommendation(None, username=user1.username, comment='Cool.', note=3)
center2_recommendation2 = Recommendation(None, username=user2.username, comment='Pourri, mais bon, 2 étoiles.', note=2)
center3_recommendation1 = Recommendation(None, username=user3.username, comment=':D', note=0)
center3_recommendation2 = Recommendation(None, username=user1.username, comment='Noice.', note=4)
center1.add_recommendation(center1_recommendation1)
center2.add_recommendation(center2_recommendation1)
center2.add_recommendation(center2_recommendation2)
center3.add_recommendation(center3_recommendation1)
center3.add_recommendation(center3_recommendation2)
