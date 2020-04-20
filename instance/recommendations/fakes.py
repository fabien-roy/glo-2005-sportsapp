from app.recommendations.models import Recommendation
from instance.practice_centers.fakes import center1, center2, center3
from instance.sports.fakes import sport1, sport2, sport3
from instance.users.fakes import user1, user3, user2

sport1_recommendation1_user1 = Recommendation(None, sport1.id, user1.username,
                                              'Un super sport. J\' adore.', 5, sport1.name)
sport2_recommendation1_user3 = Recommendation(None, sport2.id, user3.username,
                                              'Cool.', 3, sport2.name)
sport2_recommendation2_user2 = Recommendation(None, sport2.id, user2.username,
                                              'Pourri.', 0, sport2.name)
sport3_recommendation1_user1 = Recommendation(None, sport3.id, user1.username,
                                              ':D', 5, sport3.name)

center1_recommendation1_user1 = Recommendation(None, center1.id, user1.username,
                                               'Un super centre. J\' adore.', 5, center1.name)
center2_recommendation1_user1 = Recommendation(None, center2.id, user1.username,
                                               'Cool.', 3, center2.name)
center2_recommendation2_user2 = Recommendation(None, center2.id, user2.username,
                                               'Pourri, mais bon, 2 étoiles.', 2, center2.name)
center3_recommendation1_user3 = Recommendation(None, center3.id,
                                               user3.username, ':D', 0, center3.name)
center3_recommendation2_user1 = Recommendation(None, center3.id,
                                               user1.username, 'Noice.', 4, center3.name)
