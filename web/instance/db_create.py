import sys
import os

print('Creating database tables for SportsApp...')

from project import conn
from project.models import Sport
from project.queries import SportQuery

try:
    # Drop all tables
    with conn.cursor() as cur:
        # TODO : Drop users table

        sql = 'DROP TABLE IF EXISTS sports'
        cur.execute(sql)

        # TODO : Drop practice_centers table

    conn.commit()

    # Create all tables
    with conn.cursor() as cur:
        # TODO : Create users table

        sql = ('CREATE TABLE sports ('
               'id int NOT NULL AUTO_INCREMENT,'
               'name varchar(50) COLLATE utf8_bin NOT NULL,'
               'PRIMARY KEY (id)'
               ') ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin'
               'AUTO_INCREMENT=1 ;')

        # TODO : Create practice_centers table

    conn.commit()

    # Fill mocked data
    # TODO : Add users mocked data

    sport1 = Sport(name='Randonnee')
    sport2 = Sport(name='Escalade')
    sport3 = Sport(name='Natation')
    SportQuery.add(sport1)
    SportQuery.add(sport2)
    SportQuery.add(sport3)

    # TODO : Add practice_centers mocked data

finally:
    conn.close()

print('...done!')
