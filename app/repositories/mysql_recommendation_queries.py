from app.repositories.mysql_queries import build_query, filter_equal


class MySQLRecommendationQuery:
    table_name = 'recommendations'

    id_col = 'id'
    username_col = 'username'
    comment_col = 'comment'
    note_col = 'note'
    date_col = 'date'

    # TODO : Get from actual queries
    sport_recommendations_table_name = 'sport_recommendations'
    sport_recommendations_recommendation_id_col = 'recommendation_id'
    practice_center_recommendations_table_name = 'practice_center_recommendations'
    practice_center_recommendations_recommendation_id_col = 'recommendation_id'

    def get(self, recommendation_id):
        operation = ('SELECT ' + self.username_col + ', ' + self.comment_col + ', ' +
                     self.note_col + ', ' + self.date_col +
                     ' FROM ' + self.table_name)

        filters = [filter_equal(self.id_col, recommendation_id)]

        return build_query(operation, filters)

    def get_sports(self, username):
        return self.get_recommendations(username, self.sport_recommendations_recommendation_id_col,
                                        self.sport_recommendations_table_name)

    def get_practice_centers(self, username):
        return self.get_recommendations(username, self.practice_center_recommendations_recommendation_id_col,
                                        self.practice_center_recommendations_table_name)

    def get_recommendations(self, username, sub_recommendation_id_col, sub_table_name):
        operation = ('SELECT ' + self.id_col + ', ' + self.username_col + ', ' + self.comment_col + ', ' +
                     self.note_col + ', ' + self.date_col +
                     ' FROM ' + self.table_name +
                     ' WHERE ' + self.username_col + ' = \'' + username + '\'' +
                     ' AND ' + self.id_col + ' IN (' +
                     '   SELECT ' + sub_recommendation_id_col +
                     '   FROM ' + sub_table_name +
                     ');')

        return build_query(operation)

    def add(self):
        operation = ('INSERT INTO ' + self.table_name +
                     ' (' + self.username_col + ', ' + self.comment_col + ', ' + self.note_col + ', ' +
                     self.date_col + ')' +
                     ' VALUES (%s, %s, %s, %s);')

        return build_query(operation)
