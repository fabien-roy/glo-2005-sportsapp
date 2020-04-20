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
