from injector import inject

from app.climates.repositories import ClimatesRepository
from app.database import Database
from app.recommendations.repositories import RecommendationsRepository
from app.repositories.mysql_sport_queries import MySQLSportsQuery
from app.repositories.mysql_tables import MySQLSportsTable
from app.sports.exceptions import SportNotFoundException
from app.sports.models import Sport
from app.sports.repositories import SportsRepository


class MySQLSportsRepository(SportsRepository):
    @inject
    def __init__(self, database: Database, climates_repository: ClimatesRepository,
                 recommendations_repository: RecommendationsRepository):
        self.database = database
        self.climates_repository = climates_repository
        self.recommendations_repository = recommendations_repository

    def get_all(self, form=None):
        all_sports = []

        try:
            with self.database.connect().cursor() as cur:
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
            with self.database.connect().cursor() as cur:
                query = MySQLSportsQuery().get(sport_id)
                cur.execute(query)

                for sport_cur in cur.fetchall():
                    climates = self.climates_repository.get_all_for_sport(sport_id)
                    recommendations = self.recommendations_repository.get_all_for_sport(sport_id)
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
            with self.database.connect().cursor() as cur:
                query = MySQLSportsQuery().add()
                cur.execute(query, sport.name)

                self.database.connect().commit()

                sport.id = cur.lastrowid

                for climate in sport.climates:
                    self.climates_repository.add_to_sport(climate, sport)
        finally:
            cur.close()
