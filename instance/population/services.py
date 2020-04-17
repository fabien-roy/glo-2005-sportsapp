from instance.announces.services import db_populate_with_announces
from instance.climates.services import db_populate_with_climates
from instance.equipments.services import db_populate_with_equipments
from instance.practice_centers.services import db_populate_practice_centers
from instance.recommendations.services import db_populate_with_recommendations
from instance.shops.services import db_populate_with_shops
from instance.sports.services import db_populate_with_sports
from instance.users.services import db_populate_with_users


class PopulationService:
    @staticmethod
    def db_populate():
        print('Populating database tables for SportsApp...')

        db_populate_with_climates()
        db_populate_with_sports()
        db_populate_practice_centers()
        db_populate_with_users()
        db_populate_with_recommendations()
        db_populate_with_shops()
        db_populate_with_equipments()
        db_populate_with_announces()

        print('...done!')
