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
        return 'DROP PROCEDURE IF EXISTS get_practice_center_average_note'

    @staticmethod
    def create_get_practice_center_average_note():
        return ('CREATE PROCEDURE get_practice_center_average_note(IN practice_center_id integer) '
                'BEGIN'
                ' SELECT AVG(R.note) AS average_note'
                '   FROM recommendations R'
                '   JOIN practice_center_recommendations S ON S.recommendation_id = R.id'
                '   WHERE S.practice_center_id = practice_center_id;'
                'END')
