class MySQLSportQuery:

    @staticmethod
    def drop_sports():
        return 'DROP TABLE IF EXISTS sports'

    @staticmethod
    def create_sports():
        return ('CREATE TABLE sports ('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'name varchar(50) NOT NULL'
                ');')

    @staticmethod
    def drop_get_sport_average_note():
        return 'DROP PROCEDURE IF EXISTS get_sport_average_note'

    @staticmethod
    def create_get_sport_average_note():
        return ('CREATE PROCEDURE get_sport_average_note(IN sport_id integer) '
                'BEGIN'
                ' SELECT AVG(R.note) AS average_note'
                '   FROM recommendations R'
                '   JOIN sport_recommendations S ON S.recommendation_id = R.id'
                '   WHERE S.sport_id = sport_id;'
                'END')
