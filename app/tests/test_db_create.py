from app import conn
from app.models import Sport
from app.queries import SportQuery


def test_db_create():
    print('Creating test database tables for SportsApp...')

    try:
        # Delete all tables
        with conn.cursor() as cur:
            # TODO : Drop users table

            cur.execute('DROP TABLE IF EXISTS sports')

            # TODO : Drop practice_centers table

        conn.commit()

        # Create all tables
        with conn.cursor() as cur:
            # TODO : Create users table

            cur.execute('CREATE TABLE sports ('
                        'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                        'name varchar(50) NOT NULL'
                        ');')

            # TODO : Create practice_centers table

        conn.commit()

    finally:
        cur.close()

    print('...done!')
