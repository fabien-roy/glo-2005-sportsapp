class MySQLUserQuery:

    @staticmethod
    def drop_users():
        return 'DROP TABLE IF EXISTS users'

    @staticmethod
    def create_users():
        return ('CREATE TABLE users ('
                'username varchar(50) NOT NULL PRIMARY KEY,'
                'email varchar(100) NOT NULL UNIQUE,'
                'creation_date timestamp NOT NULL,'
                'last_login_date timestamp NULL,'
                'first_name varchar(50) NULL,'
                'last_name varchar(50) NULL,'
                'phone_number varchar(20) NULL'
                ');')
