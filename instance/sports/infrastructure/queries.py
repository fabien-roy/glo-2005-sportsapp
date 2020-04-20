class MySQLRecommendationQuery:

    @staticmethod
    def drop_sport_recommendations():
        return 'DROP TABLE IF EXISTS sport_recommendations'

    @staticmethod
    def drop_practice_center_recommendations():
        return 'DROP TABLE IF EXISTS practice_center_recommendations'

    @staticmethod
    def drop_recommendations():
        return 'DROP TABLE IF EXISTS recommendations'

