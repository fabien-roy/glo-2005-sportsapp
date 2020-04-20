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
