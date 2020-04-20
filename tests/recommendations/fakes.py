from instance.recommendations.fakes import sport1_recommendation1_user1, \
    sport2_recommendation1_user3, sport2_recommendation2_user2, sport3_recommendation1_user1, \
    center1_recommendation1_user1, center2_recommendation1_user1, center2_recommendation2_user2, \
    center3_recommendation1_user3, center3_recommendation2_user1

from tests.practice_centers.fakes import center1, center2, center3, get_practice_center
from tests.sports.fakes import sport1, sport2, sport3, get_sport
from tests.users.fakes import user1, user3, user2, get_user

sport1_recommendation1_user1.id = 1
sport1_recommendation1_user1.item_id = sport1.id

sport2_recommendation1_user3.id = 2
sport2_recommendation1_user3.item_id = sport2.id

sport2_recommendation2_user2.id = 3
sport2_recommendation2_user2.item_id = sport2.id

sport3_recommendation1_user1.id = 4
sport3_recommendation1_user1.item_id = sport3.id

sport1.add_recommendation(sport1_recommendation1_user1)
sport2.add_recommendation(sport2_recommendation1_user3)
sport2.add_recommendation(sport2_recommendation2_user2)
sport3.add_recommendation(sport3_recommendation1_user1)

center1_recommendation1_user1.id = 1
center1_recommendation1_user1.item_id = center1.id

center2_recommendation1_user1.id = 2
center2_recommendation1_user1.item_id = center2.id

center2_recommendation2_user2.id = 3
center2_recommendation2_user2.item_id = center2.id

center3_recommendation1_user3.id = 4
center3_recommendation1_user3.item_id = center3.id

center3_recommendation2_user1.id = 5
center3_recommendation2_user1.item_id = center3.id

center1.add_recommendation(center1_recommendation1_user1)
center2.add_recommendation(center2_recommendation1_user1)
center2.add_recommendation(center2_recommendation2_user2)
center3.add_recommendation(center3_recommendation1_user3)
center3.add_recommendation(center3_recommendation2_user1)

user1.add_sport_recommendation(sport1_recommendation1_user1)
user1.add_sport_recommendation(sport3_recommendation1_user1)
user2.add_sport_recommendation(sport2_recommendation2_user2)
user3.add_sport_recommendation(sport2_recommendation1_user3)

user1.add_practice_center_recommendation(center1_recommendation1_user1)
user1.add_practice_center_recommendation(center2_recommendation1_user1)
user1.add_practice_center_recommendation(center3_recommendation2_user1)
user2.add_practice_center_recommendation(center2_recommendation2_user2)
user3.add_practice_center_recommendation(center3_recommendation1_user3)


def get_recommendations_for_sport(sport_id):
    return get_sport(sport_id).recommendations


def get_recommendations_for_practice_center(practice_center_id):
    return get_practice_center(practice_center_id).recommendations


def get_recommendations_for_sport_and_user(user_id):
    return get_user(user_id).sport_recommendations


def get_recommendations_for_practice_center_and_user(user_id):
    return get_user(user_id).practice_center_recommendations
