from app.recommendations.models import Recommendation

from tests.practice_centers.fakes import center1, center2, center3, get_practice_center
from tests.sports.fakes import sport1, sport2, sport3, get_sport
from tests.users.fakes import user1, user3, user2, get_user

sport1_recommendation1_user1 = Recommendation(1, sport1.id, user1.username, 'Un super sport. J\' adore.', 5,
                                              sport1.name)
sport2_recommendation1_user3 = Recommendation(2, sport2.id, user3.username, 'Cool.', 3, sport2.name)
sport2_recommendation2_user2 = Recommendation(3, sport2.id, user2.username, 'Pourri.', 0, sport2.name)
sport3_recommendation1_user1 = Recommendation(4, sport3.id, user1.username, ':D', 5, sport3.name)
sport1.add_recommendation(sport1_recommendation1_user1)
sport2.add_recommendation(sport2_recommendation1_user3)
sport2.add_recommendation(sport2_recommendation2_user2)
sport3.add_recommendation(sport3_recommendation1_user1)

center1_recommendation1_user1 = Recommendation(1, center1.id, user1.username, 'Un super centre. J\' adore.', 5,
                                               center1.name)
center2_recommendation1_user1 = Recommendation(2, center2.id, user1.username, 'Cool.', 3, center2.name)
center2_recommendation2_user2 = Recommendation(3, center2.id, user2.username, 'Pourri, mais bon, 2 étoiles.', 2,
                                               center2.name)
center3_recommendation1_user3 = Recommendation(4, center3.id, user3.username, ':D', 0, center3.name)
center3_recommendation2_user1 = Recommendation(5, center3.id, user1.username, 'Noice.', 4, center3.name)
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
