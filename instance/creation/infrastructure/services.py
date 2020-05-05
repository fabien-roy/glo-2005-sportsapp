from injector import inject

from app.interfaces.database import Database
from instance.admin.infrastructure.queries import MySQLStatQuery as StatQuery
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
                self.drop_functions(cur)
                self.create_tables(cur)
                self.create_indexes(cur)
                self.create_functions(cur)
                self.create_triggers(cur)
                self.add_event_types(cur)
        finally:
            cur.close()

        print('...done!')

    def drop_tables(self, cur):
        cur.execute(StatQuery().drop_stat_events())
        cur.execute(StatQuery().drop_stat_event_types())

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

        cur.execute(UserQuery().drop_passwords())
        cur.execute(UserQuery().drop_users())

        self.database.connect().commit()

    def drop_functions(self, cur):
        cur.execute(SportQuery().drop_get_sport_average_note())
        cur.execute(PracticeCenterQuery().drop_get_practice_center_average_note())

        self.database.connect().commit()

    def create_tables(self, cur):
        cur.execute(StatQuery().create_stat_event_types())
        cur.execute(StatQuery().create_stat_events())

        cur.execute(UserQuery().create_users())
        cur.execute(UserQuery().create_passwords())

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

    def create_indexes(self, cur):
        cur.execute(SportQuery().create_btree_index())
        cur.execute(PracticeCenterQuery().create_btree_index())
        cur.execute(ShopQuery().create_btree_index())
        cur.execute(EquipmentTypeQuery().create_btree_index())
        cur.execute(ManufacturerQuery().create_btree_index())
        cur.execute(EquipmentQuery().create_btree_index())

        self.database.connect().commit()

    def create_functions(self, cur):
        cur.execute(SportQuery().create_get_sport_average_note())
        cur.execute(PracticeCenterQuery().create_get_practice_center_average_note())

        self.database.connect().commit()

    def create_triggers(self, cur):
        cur.execute(UserQuery().create_report_user_register())
        cur.execute(RecommendationQuery().create_validate_recommendation_note())
        cur.execute(RecommendationQuery().create_report_recommendation_add())

        self.database.connect().commit()

    def add_event_types(self, cur):
        cur.execute(StatQuery().add_stat_event_types('USER_LOGIN'))
        cur.execute(StatQuery().add_stat_event_types('USER_REGISTER'))
        cur.execute(StatQuery().add_stat_event_types('RECOMMENDATION_ADD'))

        self.database.connect().commit()
