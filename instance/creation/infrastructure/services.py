from injector import inject

from app.interfaces.database import Database
from instance.announces.infrastructure.queries import MySQLAnnounceQuery as AnnounceQuery
from instance.climates.infrastructure.queries import MySQLClimateQuery as ClimateQuery
from instance.equipments.infrastructure.queries import MySQLEquipmentQuery as EquipmentQuery
from instance.practice_centers.infrastructure.queries import MySQLPracticeCenterQuery \
    as PracticeCenterQuery
from instance.recommendations.infrastructure.queries import MySQLRecommendationQuery \
    as RecommendationQuery
from instance.shops.infrastructure.queries import MySQLShopQuery as ShopQuery
from instance.sports.infrastructure.queries import MySQLSportQuery as SportQuery
from instance.users.infrastructure.queries import MySQLUserQuery as UserQuery
from instance.manufacturers.infrastructure.queries import \
    MySQLManufacturerQuery as ManufacturerQuery
from instance.equipment_types.infrastructure.queries import MySQLEquipmentTypeQuery as \
    EquipmentTypeQuery


class MySQLCreationService:
    @inject
    def __init__(self, database: Database):
        self.database = database

    def db_create(self):
        print('Creating database tables for SportsApp...')

        try:
            with self.database.connect().cursor() as cur:
                self.drop_tables(cur)
                self.create_tables(cur)
                self.create_triggers(cur)
        finally:
            cur.close()

        print('...done!')

    def drop_tables(self, cur):
        cur.execute(ClimateQuery().drop_sport_climates())
        cur.execute(RecommendationQuery().drop_sport_recommendations())
        cur.execute(EquipmentTypeQuery().drop_sport_equipment_types())
        cur.execute(SportQuery().drop_sports())

        cur.execute(ClimateQuery().drop_practice_center_climates())
        cur.execute(RecommendationQuery().drop_practice_center_recommendations())
        cur.execute(PracticeCenterQuery().drop_practice_centers())

        cur.execute(ClimateQuery().drop_climates())

        cur.execute(AnnounceQuery().drop_announces())
        cur.execute(EquipmentQuery().drop_equipments())
        cur.execute(EquipmentTypeQuery().drop_equipment_types())
        cur.execute(ManufacturerQuery().drop_manufacturers())
        cur.execute(ShopQuery().drop_shops())

        cur.execute(RecommendationQuery().drop_recommendations())

        cur.execute(UserQuery().drop_users())

        self.database.connect().commit()

    def create_tables(self, cur):
        cur.execute(UserQuery().create_users())

        cur.execute(SportQuery().create_sports())

        cur.execute(PracticeCenterQuery().create_practice_centers())

        cur.execute(ClimateQuery().create_climates())
        cur.execute(ClimateQuery().create_sport_climates())
        cur.execute(ClimateQuery().create_practice_center_climates())

        cur.execute(RecommendationQuery().create_recommendations())
        cur.execute(RecommendationQuery().create_sport_recommendations())
        cur.execute(RecommendationQuery().create_practice_center_recommendations())

        cur.execute(ShopQuery().create_shops())
        cur.execute(ManufacturerQuery().create_manufacturers())
        cur.execute(EquipmentTypeQuery().create_equipment_types())
        cur.execute(EquipmentTypeQuery().create_sport_equipment_types())
        cur.execute(EquipmentQuery().create_equipments())
        cur.execute(AnnounceQuery().create_announces())

        self.database.connect().commit()

    def create_triggers(self, cur):
        cur.execute(RecommendationQuery().create_validate_recommendation_note())

        self.database.connect().commit()
