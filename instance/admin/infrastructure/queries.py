class MySQLStatQuery:

    @staticmethod
    def drop_stat_event_types():
        return 'DROP TABLE IF EXISTS stat_event_types'

    @staticmethod
    def drop_stat_events():
        return 'DROP TABLE IF EXISTS stat_events'

    @staticmethod
    def create_stat_event_types():
        return 'CREATE TABLE stat_event_types(name varchar(20) PRIMARY KEY)'

    @staticmethod
    def create_stat_events():
        return ('CREATE TABLE stat_events('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'type_name varchar(20) NOT NULL,'
                'date timestamp,'
                'FOREIGN KEY (type_name) REFERENCES stat_event_types(name) ON DELETE CASCADE);')

    @staticmethod
    def add_stat_event_types():
        return ('INSERT INTO stat_event_types (name) VALUES (\'USER_REGISTER\');'
                'INSERT INTO stat_event_types (name) VALUES (\'USER_LOGIN\');'
                'INSERT INTO stat_event_types (name) VALUES (\'RECOMMENDATION_ADD\');')
