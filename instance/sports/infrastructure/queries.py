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
        return 'DROP FUNCTION IF EXISTS get_sport_average_note'

    @staticmethod
    def create_get_sport_average_note():
        return ('CREATE FUNCTION get_sport_average_note(sport_id integer) '
                'RETURNS decimal(10,2) '
                'DETERMINISTIC '
                'BEGIN'
                ' DECLARE average decimal(10,2);'
                ' SET average = 0;'
                ' SELECT AVG(R.note) INTO average'
                '   FROM recommendations R'
                '   JOIN sport_recommendations S ON S.recommendation_id = R.id'
                '   WHERE S.sport_id = sport_id;'
                ' RETURN average;'
                'END')
