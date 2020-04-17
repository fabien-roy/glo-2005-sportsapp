from injector import inject

from app.interfaces.database import Database


class MySQLCreationService:
    @inject
    def __init__(self, database: Database):
        self.database = database

    def db_create(self):
        print('Creating database tables for SportsApp...')

        try:
            with self.database.connect().cursor() as cur:
                self.drop_tables(cur)
                self.create_tables(cur)
        finally:
            cur.close()

        print('...done!')

    def drop_tables(self, cur):
        cur.execute('DROP TABLE IF EXISTS sport_climates')
        cur.execute('DROP TABLE IF EXISTS sport_recommendations')
        cur.execute('DROP TABLE IF EXISTS sports')
        cur.execute('DROP TABLE IF EXISTS practice_center_climates')
        cur.execute('DROP TABLE IF EXISTS practice_center_recommendations')
        cur.execute('DROP TABLE IF EXISTS practice_centers')
        cur.execute('DROP TABLE IF EXISTS climates')
        cur.execute('DROP TABLE IF EXISTS recommendations')
        cur.execute('DROP TABLE IF EXISTS users')
        cur.execute('DROP TABLE IF EXISTS announces')
        cur.execute('DROP TABLE IF EXISTS shops')
        cur.execute('DROP TABLE IF EXISTS equipments')

        self.database.connect().commit()

    def create_tables(self, cur):
        cur.execute('CREATE TABLE users ('
                    'username varchar(50) NOT NULL PRIMARY KEY,'
                    'email varchar(100) NOT NULL UNIQUE,'
                    'creation_date timestamp NOT NULL,'
                    'last_login_date timestamp NULL,'
                    'first_name varchar(50) NULL,'
                    'last_name varchar(50) NULL,'
                    'phone_number varchar(20) NULL'
                    ');')

        cur.execute('CREATE TABLE sports ('
                    'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    'name varchar(50) NOT NULL'
                    ');')

        cur.execute('CREATE TABLE practice_centers ('
                    'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    'name varchar(100) NOT NULL,'
                    'email varchar(100) NULL,'
                    'web_site varchar(200) NULL,'
                    'phone_number varchar(20) NULL'
                    ');')

        cur.execute('CREATE TABLE climates ('
                    'name varchar(50) NOT NULL PRIMARY KEY'
                    ');')

        cur.execute('CREATE TABLE sport_climates ('
                    'sport_id int NOT NULL,'
                    'climate_name varchar(50) NOT NULL,'
                    'PRIMARY KEY (sport_id, climate_name),'
                    'FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE,'
                    'FOREIGN KEY (climate_name) REFERENCES climates(name) ON DELETE CASCADE'
                    ');')

        cur.execute('CREATE TABLE practice_center_climates ('
                    'practice_center_id int NOT NULL,'
                    'climate_name varchar(50) NOT NULL,'
                    'PRIMARY KEY (practice_center_id, climate_name),'
                    'FOREIGN KEY (practice_center_id) REFERENCES practice_centers(id) ON DELETE CASCADE,'
                    'FOREIGN KEY (climate_name) REFERENCES climates(name) ON DELETE CASCADE'
                    ');')

        cur.execute('CREATE TABLE recommendations ('
                    'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    'username varchar(50) NOT NULL,'
                    'comment varchar(1000) NOT NULL,'
                    'note int NOT NULL,'
                    'date timestamp NOT NULL,'
                    'FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE'
                    ');')

        cur.execute('CREATE TABLE sport_recommendations ('
                    'sport_id int NOT NULL,'
                    'recommendation_id int NOT NULL,'
                    'PRIMARY KEY (sport_id, recommendation_id),'
                    'FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE,'
                    'FOREIGN KEY (recommendation_id) REFERENCES recommendations(id) ON DELETE CASCADE'
                    ');')

        cur.execute('CREATE TABLE practice_center_recommendations ('
                    'practice_center_id int NOT NULL,'
                    'recommendation_id int NOT NULL,'
                    'PRIMARY KEY (practice_center_id, recommendation_id),'
                    'FOREIGN KEY (practice_center_id) REFERENCES practice_centers(id) ON DELETE CASCADE,'
                    'FOREIGN KEY (recommendation_id) REFERENCES recommendations(id) ON DELETE CASCADE'
                    ');')

        cur.execute('CREATE TABLE shops('
                    'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    'name varchar(100),'
                    'email varchar(100) NULL,'
                    'web_site varchar(200) NULL,'
                    'phone_number varchar(20) NULL'
                    ');')

        cur.execute('CREATE TABLE equipments('
                    'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    'category varchar(50),'
                    'name varchar(100),'
                    'description varchar(1000)'
                    ');')

        cur.execute('CREATE TABLE announces('
                    'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    'shop_id int NOT NULL,'
                    'equipment_id int NOT NULL,'
                    'state varchar(100),'
                    'price decimal,'
                    'date timestamp,'
                    'FOREIGN KEY (shop_id) REFERENCES shops(id) ON DELETE CASCADE,'
                    'FOREIGN KEY (equipment_id) REFERENCES equipments(id) ON DELETE CASCADE'
                    ');')

        self.database.connect().commit()