from datetime import datetime

from injector import inject

from app.admin.models import StatEvent
from app.admin.repositories import StatEventRepository

event_types = ['USER_REGISTER', 'USER_LOGIN', 'RECOMMENDATION_ADD']


class StatService:
    @inject
    def __init__(self, stat_event_repository: StatEventRepository):
        self.stat_event_repository = stat_event_repository

    def get_all_stat_event_sums(self):
        all_events = self.stat_event_repository.get_all()
        return self.build_stat_event_sums(all_events)

    def add_user_register(self):
        self.add_event('USER_REGISTER')

    def add_user_login(self):
        self.add_event('USER_LOGIN')

    def add_recommendation_add(self):
        self.add_event('RECOMMENDATION_ADD')

    def add_event(self, event_type):
        date = datetime.now()
        event = StatEvent(event_type, date)
        self.stat_event_repository.add(event)

    @staticmethod
    def build_stat_event_sums(events):
        stat_event_sums = {}

        for event_type in event_types:
            stat_event_sums[event_type] = 0

        for event in events:
            for event_type in event_types:
                if event.type_name == event_type:
                    stat_event_sums[event_type] += 1

        return stat_event_sums
