from app import conn
from app.climates.models import Climate
from app.sports.models import Sport
from app.sports.exceptions import SportNotFoundException
from app.sports.repositories import SportRepository


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


class MySQLSportRepository(SportRepository):
    table_name = 'sports'

    id_col = 'id'
    name_col = 'name'

    sport_climate_repository = MySQLSportClimateRepository()

    def get_all(self):
        all_sports = []

        try:
            with conn.cursor() as cur:
                cur.execute('SELECT ' + self.id_col + ', ' + self.name_col +
                            ' FROM ' + self.table_name +
                            ' ORDER BY ' + self.name_col + ';')

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
                sql = ('SELECT ' + self.id_col + ', ' + self.name_col +
                       ' FROM ' + self.table_name +
                       ' WHERE ' + self.id_col + ' = %s;')
                cur.execute(sql, sport_id)

                # TODO : Use fetchone (causes integer error)
                for sport_cur in cur.fetchall():
                    climates = self.sport_climate_repository.get_climates(sport_cur[self.id_col])
                    sport = Sport(sport_cur[self.id_col], sport_cur[self.name_col], climates)
        finally:
            cur.close()

        if sport is None:
            raise SportNotFoundException

        return sport

    def add(self, sport):
        try:
            with conn.cursor() as cur:
                sql = ('INSERT INTO ' + self.table_name +
                       ' (' + self.id_col + ', ' + self.name_col + ')' +
                       ' VALUES (%s, %s);')
                cur.execute(sql, (sport.id, sport.name))

                conn.commit()

                for climate in sport.climates:
                    self.sport_climate_repository.add(sport, climate)
        finally:
            cur.close()

        return cur.lastrowid
