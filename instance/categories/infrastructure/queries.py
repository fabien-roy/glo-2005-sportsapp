class MySQLCategoryQuery:

    @staticmethod
    def drop_categories():
        return 'DROP TABLE IF EXISTS categories'

    @staticmethod
    def create_categories():
        return ('CREATE TABLE categories('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'name varchar(100)'
                ');')
