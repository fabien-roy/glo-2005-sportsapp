from app.repositories.mysql_queries import build_query, filter_equal


class MySQLRecommendationQuery:
    table_name = 'recommendations'

    id_col = 'id'
    item_id_fake_col = 'item_id'
    username_col = 'username'
    comment_col = 'comment'
    note_col = 'note'
    name_fake_col = 'name'
    date_col = 'date'

    # TODO : Get from actual queries
    sport_table_name = 'sports'
    sport_id_col = 'id'
    sport_name_col = 'name'
    sport_recommendations_table_name = 'sport_recommendations'
    sport_recommendations_recommendation_id_col = 'recommendation_id'
    sport_recommendations_sport_id_col = 'sport_id'
    practice_center_table_name = 'practice_centers'
    practice_center_id_col = 'id'
    practice_center_name_col = 'name'
    practice_center_recommendations_table_name = 'practice_center_recommendations'
    practice_center_recommendations_recommendation_id_col = 'recommendation_id'
    practice_center_recommendations_practice_center_id_col = 'practice_center_id'

    def get_sport_recommendations(self, sport_id):
        return self.get_recommendations(sport_id,
                                        self.sport_recommendations_table_name,
                                        self.sport_recommendations_recommendation_id_col,
                                        self.sport_recommendations_sport_id_col,
                                        self.sport_table_name,
                                        self.sport_id_col,
                                        self.sport_name_col)

    def get_practice_center_recommendations(self, practice_center_id):
        return self.get_recommendations(practice_center_id,
                                        self.practice_center_recommendations_table_name,
                                        self.practice_center_recommendations_recommendation_id_col,
                                        self.practice_center_recommendations_practice_center_id_col,
                                        self.practice_center_table_name,
                                        self.practice_center_id_col,
                                        self.practice_center_name_col)

    def get_recommendations(self, item_id, sub_table_name, sub_recommendation_id_col, sub_item_id_col,
                            other_table_name, other_id_col, other_name_col):
        operation = ('SELECT T.' + self.id_col +
                     '    , ' + self.username_col +
                     '    , O.' + other_id_col + ' AS ' + self.item_id_fake_col +
                     '    , ' + self.comment_col +
                     '    , ' + self.note_col +
                     '    , O.' + other_name_col + ' AS ' + self.name_fake_col +
                     '    , ' + self.date_col +
                     ' FROM ' + self.table_name + ' T' +
                     ' JOIN ' + other_table_name + ' O ON O.' + other_id_col + ' = ' + str(item_id) +
                     ' WHERE T.' + self.id_col + ' IN (' +
                     '     SELECT ' + sub_recommendation_id_col +
                     '     FROM ' + sub_table_name +
                     '     WHERE ' + sub_item_id_col + ' = ' + str(item_id) +
                     ')')

        return build_query(operation)

    def get_sport_recommendations_for_user(self, username):
        return self.get_recommendations_for_user(username,
                                                 self.sport_recommendations_table_name,
                                                 self.sport_recommendations_recommendation_id_col,
                                                 self.sport_recommendations_sport_id_col,
                                                 self.sport_table_name,
                                                 self.sport_id_col,
                                                 self.sport_name_col)

    def get_practice_center_recommendations_for_user(self, username):
        return self.get_recommendations_for_user(username,
                                                 self.practice_center_recommendations_table_name,
                                                 self.practice_center_recommendations_recommendation_id_col,
                                                 self.practice_center_recommendations_practice_center_id_col,
                                                 self.practice_center_table_name,
                                                 self.practice_center_id_col,
                                                 self.practice_center_name_col)

    def get_recommendations_for_user(self, username, sub_table_name, sub_recommendation_id_col, sub_item_id_col,
                                     other_table_name, other_id_col, other_name_col):
        operation = ('SELECT T.' + self.id_col +
                     '    , ' + self.username_col +
                     '    , O.' + other_id_col + ' AS ' + self.item_id_fake_col +
                     '    , ' + self.comment_col +
                     '    , ' + self.note_col +
                     '    , O.' + other_name_col + ' AS ' + self.name_fake_col +
                     '    , ' + self.date_col +
                     ' FROM ' + self.table_name + ' AS T' +
                     ' JOIN ' + sub_table_name + ' S ON S.' + sub_recommendation_id_col + ' = ' + self.id_col +
                     ' JOIN ' + other_table_name + ' O ON O.' + other_id_col + ' = S.' + sub_item_id_col +
                     ' WHERE ' + self.username_col + ' = \'' + username + '\'' +
                     ' AND T.' + self.id_col + ' IN (' +
                     '   SELECT ' + sub_recommendation_id_col +
                     '   FROM ' + sub_table_name +
                     ')')

        return build_query(operation)

    def add(self):
        operation = ('INSERT INTO ' + self.table_name +
                     ' (' + self.username_col + ', ' + self.comment_col + ', ' + self.note_col + ', ' +
                     self.date_col + ')' +
                     ' VALUES (%s, %s, %s, %s)')

        return build_query(operation)
