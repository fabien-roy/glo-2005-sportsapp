from injector import inject

from app.admin.models import StatEvent
from app.admin.repositories import StatEventRepository
from app.interfaces.database import Database
from app.admin.infrastructure.queries import MySQLStatEventQuery as Query
from app.admin.infrastructure.tables import MySQLStatEventsTable as StatEvents


class MySQLStatEventRepository(StatEventRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_all(self):
        all_events = []

        try:
            with self.database.connect().cursor() as cur:
                query = Query().get_all()
                cur.execute(query)

                for stat_cur in cur.fetchall():
                    practice_center = self.build_stat(stat_cur)
                    all_events.append(practice_center)
        finally:
            cur.close()

        return all_events

    @staticmethod
    def build_stat(cur):
        return StatEvent(cur[StatEvents.type_name_col], cur[StatEvents.date_col])

    def add(self, event):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().add()
                cur.execute(query, (event.type_name, event.date))

                self.database.connect().commit()
        finally:
            cur.close()
