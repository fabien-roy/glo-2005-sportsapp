class MySQLClimateQuery:

    @staticmethod
    def drop_sport_climates():
        return 'DROP TABLE IF EXISTS sport_climates'

    @staticmethod
    def create_sport_climates():
        return ('CREATE TABLE sport_climates ('
                'sport_id int NOT NULL,'
                'climate_name varchar(50) NOT NULL,'
                'PRIMARY KEY (sport_id, climate_name),'
                'FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE,'
                'FOREIGN KEY (climate_name) REFERENCES climates(name) ON DELETE CASCADE'
                ');')

    @staticmethod
    def drop_practice_center_climates():
        return 'DROP TABLE IF EXISTS practice_center_climates'

    @staticmethod
    def create_practice_center_climates():
        return ('CREATE TABLE practice_center_climates ('
                'practice_center_id int NOT NULL,'
                'climate_name varchar(50) NOT NULL,'
                'PRIMARY KEY (practice_center_id, climate_name),'
                'FOREIGN KEY (practice_center_id) REFERENCES practice_centers(id) ON DELETE CASCADE,'
                'FOREIGN KEY (climate_name) REFERENCES climates(name) ON DELETE CASCADE'
                ');')

    @staticmethod
    def drop_climates():
        return 'DROP TABLE IF EXISTS climates'

    @staticmethod
    def create_climates():
        return ('CREATE TABLE climates ('
                'name varchar(50) NOT NULL PRIMARY KEY'
                ');')
