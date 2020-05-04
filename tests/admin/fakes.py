from datetime import datetime

from app.admin.models import StatEvent

now = datetime.now()
event1 = StatEvent('USER_LOGIN', now)
event2 = StatEvent('USER_REGISTER', now)
event3 = StatEvent('RECOMMENDATION_ADD', now)


def get_events():
    return [event1, event2, event3]


def get_nonnull_stat_event_sums():
    return {(event1, 0), (event2, 0), (event3, 0)}


def get_null_stat_event_sums():
    return {(event1, 1), (event2, 1), (event3, 1)}
