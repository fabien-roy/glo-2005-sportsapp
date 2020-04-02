from app.tests.fakes import user1, user2, user3, sport3, sport2, sport1, center3, center2, center1


def get_climates_for_practice_center(practice_center_id):
    return get_practice_center(practice_center_id).climates


def get_recommendations_for_practice_center(practice_center_id):
    return get_practice_center(practice_center_id).recommendations


def get_practice_center(practice_center_id):
    if practice_center_id == center1.id:
        return center1
    if practice_center_id == center2.id:
        return center2
    if practice_center_id == center3.id:
        return center3


def get_climates_for_sport(sport_id):
    return get_sport(sport_id).climates


def get_recommendations_for_sport(sport_id):
    return get_sport(sport_id).recommendations


def get_sport(sport_id):
    if sport_id == sport1.id:
        return sport1
    if sport_id == sport2.id:
        return sport2
    if sport_id == sport3.id:
        return sport3


def get_recommendations_for_sport_and_user(user_id):
    return get_user(user_id).sport_recommendations


def get_recommendations_for_practice_center_and_user(user_id):
    return get_user(user_id).practice_center_recommendations


def get_user(username):
    if username == user1.username:
        return user1
    if username == user2.username:
        return user2
    if username == user3.username:
        return user3
