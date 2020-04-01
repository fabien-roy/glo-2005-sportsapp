from app.repositories.mysql_queries import build_query
from app.repositories.mysql_tables import MySQLRecommendationsTable, MySQLSportRecommendationsTable, MySQLSportsTable, \
    MySQLPracticeCenterRecommendationsTable, MySQLPracticeCentersTable


class MySQLRecommendationQuery:
    item_id_fake_col = 'item_id'
    name_fake_col = 'name'

    def get_sport_recommendations(self, sport_id):
        return self.get_recommendations(sport_id,
                                        MySQLSportRecommendationsTable.table_name,
                                        MySQLSportRecommendationsTable.recommendation_id_col,
                                        MySQLSportRecommendationsTable.sport_id_col,
                                        MySQLSportsTable.table_name,
                                        MySQLSportsTable.id_col,
                                        MySQLSportsTable.name_col)

    def get_practice_center_recommendations(self, practice_center_id):
        return self.get_recommendations(practice_center_id,
                                        MySQLPracticeCenterRecommendationsTable.table_name,
                                        MySQLPracticeCenterRecommendationsTable.recommendation_id_col,
                                        MySQLPracticeCenterRecommendationsTable.practice_center_id_col,
                                        MySQLPracticeCentersTable.table_name,
                                        MySQLPracticeCentersTable.id_col,
                                        MySQLPracticeCentersTable.name_col)

    def get_recommendations(self, item_id, sub_table_name, sub_recommendation_id_col, sub_item_id_col,
                            other_table_name, other_id_col, other_name_col):
        operation = ('SELECT T.' + MySQLRecommendationsTable.id_col +
                     ', ' + MySQLRecommendationsTable.username_col +
                     ', O.' + other_id_col + ' AS ' + self.item_id_fake_col +
                     ', ' + MySQLRecommendationsTable.comment_col +
                     ', ' + MySQLRecommendationsTable.note_col +
                     ', O.' + other_name_col + ' AS ' + self.name_fake_col +
                     ', ' + MySQLRecommendationsTable.date_col +
                     ' FROM ' + MySQLRecommendationsTable.table_name + ' T' +
                     ' JOIN ' + other_table_name + ' O ON O.' + other_id_col + ' = ' + str(item_id) +
                     ' WHERE T.' + MySQLRecommendationsTable.id_col + ' IN (' +
                     '     SELECT ' + sub_recommendation_id_col +
                     '     FROM ' + sub_table_name +
                     '     WHERE ' + sub_item_id_col + ' = ' + str(item_id) +
                     ')')

        return build_query(operation)

    def get_sport_recommendations_for_user(self, username):
        return self.get_recommendations_for_user(username,
                                                 MySQLSportRecommendationsTable.table_name,
                                                 MySQLSportRecommendationsTable.recommendation_id_col,
                                                 MySQLSportRecommendationsTable.sport_id_col,
                                                 MySQLSportsTable.table_name,
                                                 MySQLSportsTable.id_col,
                                                 MySQLSportsTable.name_col)

    def get_practice_center_recommendations_for_user(self, username):
        return self.get_recommendations_for_user(username,
                                                 MySQLPracticeCenterRecommendationsTable.table_name,
                                                 MySQLPracticeCenterRecommendationsTable.recommendation_id_col,
                                                 MySQLPracticeCenterRecommendationsTable.practice_center_id_col,
                                                 MySQLPracticeCentersTable.table_name,
                                                 MySQLPracticeCentersTable.id_col,
                                                 MySQLPracticeCentersTable.name_col)

    def get_recommendations_for_user(self, username, sub_table_name, sub_recommendation_id_col, sub_item_id_col,
                                     other_table_name, other_id_col, other_name_col):
        operation = ('SELECT T.' + MySQLRecommendationsTable.id_col +
                     ', ' + MySQLRecommendationsTable.username_col +
                     ', O.' + other_id_col + ' AS ' + self.item_id_fake_col +
                     ', ' + MySQLRecommendationsTable.comment_col +
                     ', ' + MySQLRecommendationsTable.note_col +
                     ', O.' + other_name_col + ' AS ' + self.name_fake_col +
                     ', ' + MySQLRecommendationsTable.date_col +
                     ' FROM ' + MySQLRecommendationsTable.table_name + ' AS T' +
                     ' JOIN ' + sub_table_name + ' S ON S.' + sub_recommendation_id_col + ' = ' +
                     MySQLRecommendationsTable.id_col +
                     ' JOIN ' + other_table_name + ' O ON O.' + other_id_col + ' = S.' + sub_item_id_col +
                     ' WHERE ' + MySQLRecommendationsTable.username_col + ' = \'' + username + '\'' +
                     ' AND T.' + MySQLRecommendationsTable.id_col + ' IN (' +
                     '   SELECT ' + sub_recommendation_id_col +
                     '   FROM ' + sub_table_name +
                     ')')

        return build_query(operation)

    def add(self):
        operation = ('INSERT INTO ' + MySQLRecommendationsTable.table_name +
                     ' (' + MySQLRecommendationsTable.username_col +
                     ', ' + MySQLRecommendationsTable.comment_col +
                     ', ' + MySQLRecommendationsTable.note_col +
                     ', ' + MySQLRecommendationsTable.date_col + ')' +
                     ' VALUES (%s, %s, %s, %s)')

        return build_query(operation)
