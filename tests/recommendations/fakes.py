from app.recommendations.models import Recommendation

from tests.practice_centers.fakes import center1, center2, center3, get_practice_center
from tests.sports.fakes import sport1, sport2, sport3, get_sport
from tests.users.fakes import user1, user3, user2, get_user

sport1_recommendation1_user1 = Recommendation(1, sport1.id, user1.username,
                                              'Un super sport. J\' adore.', 5, sport1.name)
sport2_recommendation1_user3 = Recommendation(2, sport2.id, user3.username,
                                              'Cool.', 3, sport2.name)
sport2_recommendation2_user2 = Recommendation(3, sport2.id, user2.username,
                                              'Pourri.', 0, sport2.name)
sport3_recommendation1_user1 = Recommendation(4, sport3.id, user1.username,
                                              ':D', 5, sport3.name)

center1_recommendation1_user1 = Recommendation(5, center1.id, user1.username,
                                               'Un super centre. J\' adore.', 5, center1.name)
center2_recommendation1_user1 = Recommendation(6, center2.id, user1.username,
                                               'Cool.', 3, center2.name)
center2_recommendation2_user2 = Recommendation(7, center2.id, user2.username,
                                               'Pourri, mais bon, 2 étoiles.', 2, center2.name)
center3_recommendation1_user3 = Recommendation(8, center3.id,
                                               user3.username, ':D', 0, center3.name)
center3_recommendation2_user1 = Recommendation(9, center3.id,
                                               user1.username, 'Noice.', 4, center3.name)

sport1.recommendations = [sport1_recommendation1_user1]
sport2.recommendations = [sport2_recommendation1_user3, sport2_recommendation2_user2]
sport3.recommendations = [sport3_recommendation1_user1]

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
