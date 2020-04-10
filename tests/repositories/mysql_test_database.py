import pymysql.cursors

from app import app
from app.database import Database


class MySQLTestDatabase(Database):
    def create_connection(self):
        return pymysql.connect(host=app.config['MYSQL_HOST'],
                               user=app.config['MYSQL_USER'],
                               password=app.config['MYSQL_PASSWORD'],
                               db=app.config['MYSQL_TEST_DB'],
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)


database = MySQLTestDatabase()
