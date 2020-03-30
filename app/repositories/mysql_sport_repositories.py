from app import conn
from app.climates.models import Climate
from app.repositories.mysql_recommendation_repositories import MySQLRecommendationsRepository
from app.repositories.mysql_sport_queries import MySQLSportsQuery
from app.sports.exceptions import SportNotFoundException
from app.sports.models import Sport
from app.sports.repositories import SportsRepository


class MySQLSportClimateRepository:
    table_name = 'sport_climates'

    sport_id_col = 'sport_id'
    climate_name_col = 'climate_name'

    def get_climates(self, sport_id):
        climates = []

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.climate_name_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.sport_id_col + ' = %s;')
                cur.execute(sql, sport_id)

                for climate_cur in cur.fetchall():
                    climate = Climate(climate_cur[self.climate_name_col])
                    climates.append(climate)
        finally:
            cur.close()

        return climates

    def add(self, sport, climate):
        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.sport_id_col + ', ' + self.climate_name_col + ')' +
                       ' VALUES (%s, %s);')
                cur.execute(sql, (sport.id, climate.name))

                conn.commit()
        finally:
            cur.close()


class MySQLSportRecommendationRepository:
    table_name = 'sport_recommendations'

    sport_id_col = 'sport_id'
    recommendation_id_col = 'recommendation_id'

    # TODO : Inject in repositories
    recommendation_repository = MySQLRecommendationsRepository()

    def get_recommendations(self, sport_id):
        recommendations = []

        try:
            with conn.cursor() as cur:
                sql = ('SELECT ' + self.recommendation_id_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.sport_id_col + ' = %s;')
                cur.execute(sql, sport_id)

                # TODO : Solve n+1 problem
                for recommendation_cur in cur.fetchall():
                    recommendation = self.recommendation_repository.get(recommendation_cur[self.recommendation_id_col])
                    recommendations.append(recommendation)
        finally:
            cur.close()

        return recommendations

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
    table_name = MySQLSportsQuery.table_name

    id_col = MySQLSportsQuery.id_col
    name_col = MySQLSportsQuery.name_col

    sport_climate_repository = MySQLSportClimateRepository()
    sport_recommendation_repository = MySQLSportRecommendationRepository()

    def get_all(self, form=None):
        all_sports = []

        try:
            with conn.cursor() as cur:
                query = MySQLSportsQuery().get_all(form)
                cur.execute(query)

                for sport_cur in cur.fetchall():
                    sport = Sport(sport_cur[self.id_col], sport_cur[self.name_col])
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
                    climates = self.sport_climate_repository.get_climates(sport_id)
                    recommendations = self.sport_recommendation_repository.get_recommendations(sport_id)
                    sport = Sport(sport_id, sport_cur[self.name_col], climates, recommendations)
        finally:
            cur.close()

        if sport is None:
            raise SportNotFoundException

        return sport

    def add(self, sport):
        try:
            with conn.cursor() as cur:
                query = MySQLSportsQuery().add()
                cur.execute(query, sport.name)

                conn.commit()

                sport.id = cur.lastrowid

                for climate in sport.climates:
                    self.sport_climate_repository.add(sport, climate)
        finally:
            cur.close()

    def add_recommendation(self, sport_id, recommendation):
        self.sport_recommendation_repository.add(sport_id, recommendation)
