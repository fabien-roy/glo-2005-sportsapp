from app.interfaces.infrastructure.queries import MySQLQuery
from app.sports.infrastructure.tables import MySQLSportTable as Sports
from app.practice_centers.infrastructure.tables import MySQLPracticeCenterTable as PracticeCenters
from app.recommendations.infrastructure.tables import MySQLRecommendationTable as Recommendations, \
    MySQLSportRecommendationTable as SportRecommendations, MySQLPracticeCenterRecommendationTable \
    as PracticeCenterRecommendations


class MySQLRecommendationQuery(MySQLQuery):
    item_id_fake_col = 'item_id'
    name_fake_col = 'name'

    def get_all_for_sport(self, sport_id):
        return self.get_all_for_type(sport_id,
                                     SportRecommendations.table_name,
                                     SportRecommendations.recommendation_id_col,
                                     SportRecommendations.sport_id_col,
                                     Sports.table_name,
                                     Sports.id_col,
                                     Sports.name_col)

    def get_all_for_practice_center(self, practice_center_id):
        return self.get_all_for_type(practice_center_id,
                                     PracticeCenterRecommendations.table_name,
                                     PracticeCenterRecommendations.recommendation_id_col,
                                     PracticeCenterRecommendations.practice_center_id_col,
                                     PracticeCenters.table_name,
                                     PracticeCenters.id_col,
                                     PracticeCenters.name_col)

    def get_all_for_type(self, item_id, sub_table_name, sub_recommendation_id_col, sub_item_id_col,
                         other_table_name, other_id_col, other_name_col):
        operation = (f'SELECT T.{Recommendations.id_col}'
                     f', {Recommendations.username_col}'
                     f', O.{other_id_col} AS {self.item_id_fake_col}'
                     f', {Recommendations.comment_col}'
                     f', {Recommendations.note_col}'
                     f', O.{other_name_col} AS {self.name_fake_col}'
                     f', {Recommendations.date_col}'
                     f' FROM {Recommendations.table_name} T'
                     f' JOIN {other_table_name} O ON O.{other_id_col}  = + {str(item_id)}'
                     f' WHERE T.{Recommendations.id_col} IN ('
                     f'     SELECT {sub_recommendation_id_col}'
                     f'     FROM {sub_table_name}'
                     f'     WHERE {sub_item_id_col} = {str(item_id)}'
                     f')')

        return self.build_query(operation)

    def get_all_for_sport_and_user(self, username):
        return self.get_all_for_type_and_user(username,
                                              SportRecommendations.table_name,
                                              SportRecommendations.recommendation_id_col,
                                              SportRecommendations.sport_id_col,
                                              Sports.table_name,
                                              Sports.id_col,
                                              Sports.name_col)

    def get_all_for_practice_center_and_user(self, username):
        return self.get_all_for_type_and_user(username,
                                              PracticeCenterRecommendations.table_name,
                                              PracticeCenterRecommendations
                                              .recommendation_id_col,
                                              PracticeCenterRecommendations
                                              .practice_center_id_col,
                                              PracticeCenters.table_name,
                                              PracticeCenters.id_col,
                                              PracticeCenters.name_col)

    def get_all_for_type_and_user(self, username, sub_table_name, sub_recommendation_id_col,
                                  sub_item_id_col,
                                  other_table_name, other_id_col, other_name_col):
        operation = (f'SELECT T.{Recommendations.id_col}'
                     f', {Recommendations.username_col}'
                     f', O.{other_id_col} AS {self.item_id_fake_col}'
                     f', {Recommendations.comment_col}'
                     f', {Recommendations.note_col}'
                     f', O.{other_name_col} AS {self.name_fake_col}'
                     f', {Recommendations.date_col}'
                     f' FROM {Recommendations.table_name} AS T'
                     f' JOIN {sub_table_name} S ON S.{sub_recommendation_id_col} = '
                     f'{Recommendations.id_col}'
                     f' JOIN {other_table_name} O ON O.{other_id_col} = S.{sub_item_id_col}'
                     f' WHERE {Recommendations.username_col} = \'{username}\''
                     f' AND T.{Recommendations.id_col} IN ('
                     f'   SELECT {sub_recommendation_id_col}'
                     f'   FROM {sub_table_name}'
                     f')')

        return self.build_query(operation)

    def add(self):
        operation = (f'INSERT INTO {Recommendations.table_name}'
                     f' ({Recommendations.username_col}'
                     f', {Recommendations.comment_col}'
                     f', {Recommendations.note_col}'
                     f', {Recommendations.date_col})'
                     f' VALUES (%s, %s, %s, %s)')

        return self.build_query(operation)

    def add_to_sport(self):
        return self.add_to_type(SportRecommendations.table_name,
                                SportRecommendations.recommendation_id_col,
                                SportRecommendations.sport_id_col)

    def add_to_practice_center(self):
        return self.add_to_type(PracticeCenterRecommendations.table_name,
                                PracticeCenterRecommendations.recommendation_id_col,
                                PracticeCenterRecommendations.practice_center_id_col)

    def add_to_type(self, table_name, recommendation_id_col, type_id_col):
        operation = (f'INSERT INTO {table_name}'
                     f' ({recommendation_id_col}'
                     f', {type_id_col})'
                     f' VALUES (%s, %s);')

        return self.build_query(operation)
