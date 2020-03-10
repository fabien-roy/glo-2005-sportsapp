from app import conn


def db_create():
    print('Creating database tables for SportsApp...')

    try:
        # Delete all tables
        with conn.cursor() as cur:
            cur.execute('DROP TABLE IF EXISTS sport_climates')

            # TODO : Drop users table

            cur.execute('DROP TABLE IF EXISTS sports')

            cur.execute('DROP TABLE IF EXISTS practice_centers')

            cur.execute('DROP TABLE IF EXISTS climates')

        conn.commit()

        # Create all tables
        with conn.cursor() as cur:
            # TODO : Create users table

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

        conn.commit()
    finally:
        cur.close()

    print('...done!')
