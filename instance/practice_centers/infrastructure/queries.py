class MySQLPracticeCenterQuery:

    @staticmethod
    def drop_practice_centers():
        return 'DROP TABLE IF EXISTS practice_centers'

    @staticmethod
    def create_practice_centers():
        return ('CREATE TABLE practice_centers ('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'name varchar(100) NOT NULL,'
                'email varchar(100) NULL,'
                'web_site varchar(200) NULL,'
                'phone_number varchar(20) NULL'
                ');')

    @staticmethod
    def drop_get_practice_center_average_note():
        return 'DROP FUNCTION IF EXISTS get_practice_center_average_note'

    @staticmethod
    def create_get_practice_center_average_note():
        return ('CREATE FUNCTION get_practice_center_average_note(practice_center_id integer) '
                'RETURNS decimal(10,2) '
                'DETERMINISTIC '
                'BEGIN'
                ' DECLARE average decimal(10,2);'
                ' SET average = 0;'
                ' SELECT AVG(R.note) INTO average'
                '   FROM recommendations R'
                '   JOIN practice_center_recommendations S ON S.recommendation_id = R.id'
                '   WHERE S.practice_center_id = practice_center_id;'
                ' RETURN average;'
                'END')
