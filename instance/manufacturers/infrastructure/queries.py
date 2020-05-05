class MySQLManufacturerQuery:

    @staticmethod
    def drop_manufacturers():
        return 'DROP TABLE IF EXISTS manufacturers'

    @staticmethod
    def create_manufacturers():
        return ('CREATE TABLE manufacturers('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'name varchar(100)'
                ');')

    @staticmethod
    def create_btree_index():
        return 'CREATE INDEX manufacturer_index ON manufacturers(name) USING BTREE;'
