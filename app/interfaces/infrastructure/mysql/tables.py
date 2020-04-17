class MySQLSportsTable:
    table_name = 'sports'
    id_col = 'id'
    name_col = 'name'


class MySQLPracticeCentersTable:
    table_name = 'practice_centers'
    id_col = 'id'
    name_col = 'name'
    email_col = 'email'
    web_site_col = 'web_site'
    phone_number_col = 'phone_number'


class MySQLShopsTable:
    table_name = 'shops'
    id_col = 'id'
    name_col = 'name'
    email_col = 'email'
    phone_number_col = 'phone_number'
    web_site_col = 'web_site'


class MySQLUsersTable:
    table_name = 'users'
    username_col = 'username'
    email_col = 'email'
    first_name_col = 'first_name'
    last_name_col = 'last_name'
    phone_number_col = 'phone_number'
    creation_date_col = 'creation_date'
    last_login_date_col = 'last_login_date'


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


class MySQLEquipmentsTable:
    table_name = 'equipments'
    id_col = 'id'
    category_col = 'category'
    name_col = 'name'
    description_col = "description"
