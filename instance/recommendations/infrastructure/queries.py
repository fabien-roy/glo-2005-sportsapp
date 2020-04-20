class MySQLRecommendationQuery:

    @staticmethod
    def drop_sport_recommendations():
        return 'DROP TABLE IF EXISTS sport_recommendations'

    @staticmethod
    def create_sport_recommendations():
        return ('CREATE TABLE sport_recommendations ('
                'sport_id int NOT NULL,'
                'recommendation_id int NOT NULL,'
                'PRIMARY KEY (sport_id, recommendation_id),'
                'FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE,'
                'FOREIGN KEY (recommendation_id) REFERENCES recommendations(id) ON DELETE CASCADE'
                ');')

    @staticmethod
    def drop_practice_center_recommendations():
        return 'DROP TABLE IF EXISTS practice_center_recommendations'

    @staticmethod
    def create_practice_center_recommendations():
        return ('CREATE TABLE practice_center_recommendations ('
                'practice_center_id int NOT NULL,'
                'recommendation_id int NOT NULL,'
                'PRIMARY KEY (practice_center_id, recommendation_id),'
                'FOREIGN KEY (practice_center_id) REFERENCES practice_centers(id) '
                'ON DELETE CASCADE,'
                'FOREIGN KEY (recommendation_id) REFERENCES recommendations(id) ON DELETE CASCADE'
                ');')

    @staticmethod
    def drop_recommendations():
        return 'DROP TABLE IF EXISTS recommendations'

    @staticmethod
    def create_recommendations():
        return ('CREATE TABLE recommendations ('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'username varchar(50) NOT NULL,'
                'comment varchar(1000) NOT NULL,'
                'note int NOT NULL,'
                'date timestamp NOT NULL,'
                'FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE'
                ');')
