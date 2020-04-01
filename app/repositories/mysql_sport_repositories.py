from app import conn
from app.repositories.mysql_climate_repositories import MySQLClimatesRepository
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_sport_queries import MySQLSportsQuery
from app.repositories.mysql_tables import MySQLSportsTable
from app.sports.exceptions import SportNotFoundException
from app.sports.models import Sport
from app.sports.repositories import SportsRepository


class MySQLSportRecommendationRepository:
    table_name = 'sport_recommendations'

    sport_id_col = 'sport_id'
    recommendation_id_col = 'recommendation_id'

    # TODO : Inject in repositories
    recommendation_repository = MySQLRecommendationsRepository()

    def add(self, sport_id, recommendation):
        self.recommendation_repository.add(recommendation)

        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.sport_id_col + ', ' + self.recommendation_id_col + ')' +
                       ' VALUES (%s, %s);')
                cur.execute(sql, (sport_id, recommendation.id))

                conn.commit()
        finally:
            cur.close()


class MySQLSportsRepository(SportsRepository):
    # TODO : Inject in repositories
    climate_repository = MySQLClimatesRepository()
    recommendation_repository = MySQLRecommendationsRepository()
    sport_recommendation_repository = MySQLSportRecommendationRepository()

    def get_all(self, form=None):
        all_sports = []

        try:
            with conn.cursor() as cur:
                query = MySQLSportsQuery().get_all(form)
                cur.execute(query)

                for sport_cur in cur.fetchall():
                    sport = self.build_sport(sport_cur)
                    all_sports.append(sport)
        finally:
            cur.close()

        return all_sports

    def get(self, sport_id):
        sport = None

        try:
            with conn.cursor() as cur:
                query = MySQLSportsQuery().get(sport_id)
                cur.execute(query)

                # TODO : Use fetchone (causes integer error)
                for sport_cur in cur.fetchall():
                    climates = self.climate_repository.get_all_for_sport(sport_id)
                    recommendations = self.recommendation_repository.get_all_for_sport(sport_id)
                    sport = self.build_sport(sport_cur, climates, recommendations)
        finally:
            cur.close()

        if sport is None:
            raise SportNotFoundException

        return sport

    @staticmethod
    def build_sport(cur, climates=None, recommendations=None):
        return Sport(cur[MySQLSportsTable.id_col],
                     cur[MySQLSportsTable.name_col],
                     climates,
                     recommendations)

    def add(self, sport):
        try:
            with conn.cursor() as cur:
                query = MySQLSportsQuery().add()
                cur.execute(query, sport.name)

                conn.commit()

                sport.id = cur.lastrowid

                for climate in sport.climates:
                    self.climate_repository.add_to_sport(climate, sport)
        finally:
            cur.close()

    def add_recommendation(self, sport_id, recommendation):
        self.sport_recommendation_repository.add(sport_id, recommendation)
