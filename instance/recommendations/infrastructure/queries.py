class MySQLClimateQuery:

    @staticmethod
    def drop_sport_climates():
        return 'DROP TABLE IF EXISTS sport_climates'

    @staticmethod
    def drop_practice_center_climates():
        return 'DROP TABLE IF EXISTS practice_center_climates'

    @staticmethod
    def drop_climates():
        return 'DROP TABLE IF EXISTS climates'

