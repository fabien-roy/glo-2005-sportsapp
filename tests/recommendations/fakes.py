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

sport1.recommendations = [sport1_recommendation1_user1]
sport2.recommendations = [sport2_recommendation1_user3, sport2_recommendation2_user2]
sport3.recommendations = [sport3_recommendation1_user1]

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

center1.recommendations = [center1_recommendation1_user1]
center2.recommendations = [center2_recommendation1_user1, center2_recommendation2_user2]
center3.recommendations = [center3_recommendation1_user3, center3_recommendation2_user1]

user1.sport_recommendations = [sport1_recommendation1_user1, sport3_recommendation1_user1]
user2.sport_recommendations = [sport2_recommendation2_user2]
user3.sport_recommendations = [sport2_recommendation1_user3]

user1.practice_center_recommendations = [center1_recommendation1_user1,
                                         center2_recommendation1_user1,
                                         center3_recommendation2_user1]
user2.practice_center_recommendations = [center2_recommendation2_user2]
user3.practice_center_recommendations = [center3_recommendation1_user3]


def get_recommendations_for_sport(sport_id):
    return get_sport(sport_id).recommendations


def get_recommendations_for_practice_center(practice_center_id):
    return get_practice_center(practice_center_id).recommendations


def get_recommendations_for_sport_and_user(username):
    return get_user(username).sport_recommendations


def get_recommendations_for_practice_center_and_user(username):
    return get_user(username).practice_center_recommendations
