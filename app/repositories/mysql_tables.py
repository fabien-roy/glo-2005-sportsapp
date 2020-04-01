class MySQLSportsTable:
    table_name = 'sports'
    id_col = 'id'
    name_col = 'name'


class MySQLPracticeCentersTable:
    table_name = 'practice_centers'
    id_col = 'id'
    name_col = 'name'


class MySQLRecommendationsTable:
    table_name = 'recommendations'

    id_col = 'id'
    username_col = 'username'
    comment_col = 'comment'
    note_col = 'note'
    date_col = 'date'


class MySQLSportRecommendationsTable:
    table_name = 'sport_recommendations'
    recommendation_id_col = 'recommendation_id'
    sport_id_col = 'sport_id'


class MySQLPracticeCenterRecommendationsTable:
    table_name = 'practice_center_recommendations'
    recommendation_id_col = 'recommendation_id'
    practice_center_id_col = 'practice_center_id'
