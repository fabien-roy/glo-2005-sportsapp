class MySQLRecommendationQuery:

    @staticmethod
    def drop_sport_recommendations():
        return 'DROP TABLE IF EXISTS sport_recommendations'

    @staticmethod
    def create_sport_recommendations():
        return ('CREATE TABLE sport_recommendations ('
                '    sport_id int NOT NULL,'
                '    recommendation_id int NOT NULL,'
                '    PRIMARY KEY (sport_id, recommendation_id),'
                '    FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE,'
                '    FOREIGN KEY (recommendation_id) REFERENCES recommendations(id)'
                '    ON DELETE CASCADE'
                ');')

    @staticmethod
    def drop_practice_center_recommendations():
        return 'DROP TABLE IF EXISTS practice_center_recommendations'

    @staticmethod
    def create_practice_center_recommendations():
        return ('CREATE TABLE practice_center_recommendations ('
                '    practice_center_id int NOT NULL,'
                '    recommendation_id int NOT NULL,'
                '    PRIMARY KEY (practice_center_id, recommendation_id),'
                '    FOREIGN KEY (practice_center_id) REFERENCES practice_centers(id) '
                '    ON DELETE CASCADE,'
                '    FOREIGN KEY (recommendation_id) REFERENCES recommendations(id)'
                '    ON DELETE CASCADE'
                ');')

    @staticmethod
    def drop_recommendations():
        return 'DROP TABLE IF EXISTS recommendations'

    @staticmethod
    def create_recommendations():
        return ('CREATE TABLE recommendations ('
                '    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                '    username varchar(50) NOT NULL,'
                '    comment varchar(1000) NOT NULL,'
                '    note int NOT NULL,'
                '    date timestamp NOT NULL,'
                '    FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE'
                ');')

    @staticmethod
    def create_validate_recommendation_note():
        return ('CREATE TRIGGER validate_recommendation_note '
                'BEFORE INSERT ON recommendations '
                'FOR EACH ROW '
                'BEGIN '
                '    IF NEW.note < 0 OR NEW.note > 5 THEN'
                "        SIGNAL SQLSTATE '45000'"
                "        SET MESSAGE_TEXT = 'Recommendation note must be between 0 and 5.';"
                '    END IF;'
                'END;')

    @staticmethod
    def create_report_recommendation_add():
        return ('CREATE TRIGGER report_recommendation_add '
                'BEFORE INSERT ON recommendations '
                'FOR EACH ROW '
                'BEGIN '
                '    INSERT INTO stat_events (type_name, date)'
                "    VALUES ('RECOMMENDATION_ADD', NOW());"
                'END;')
