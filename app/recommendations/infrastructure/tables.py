class MySQLRecommendationTable:
    table_name = 'recommendations'

    id_col = 'id'
    username_col = 'username'
    comment_col = 'comment'
    note_col = 'note'
    date_col = 'date'


class MySQLSportRecommendationTable:
    table_name = 'sport_recommendations'
    recommendation_id_col = 'recommendation_id'
    sport_id_col = 'sport_id'


class MySQLPracticeCenterRecommendationTable:
    table_name = 'practice_center_recommendations'
    recommendation_id_col = 'recommendation_id'
    practice_center_id_col = 'practice_center_id'
