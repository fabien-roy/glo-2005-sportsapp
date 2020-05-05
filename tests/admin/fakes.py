from datetime import datetime

from app.admin.models import StatEvent

now = datetime.now()
user_login_event = StatEvent('USER_LOGIN', now)
user_register_event = StatEvent('USER_REGISTER', now)
recommendation_add_event = StatEvent('RECOMMENDATION_ADD', now)


events = [user_login_event, user_register_event, recommendation_add_event]


nonnull_stat_event_sums = {(user_login_event, 0), (user_register_event, 0),
                           (recommendation_add_event, 0)}

null_stat_event_sums = {(user_login_event, 1), (user_register_event, 1),
                        (recommendation_add_event, 1)}
