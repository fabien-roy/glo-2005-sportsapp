class MySQLShopQuery:

    @staticmethod
    def drop_shops():
        return 'DROP TABLE IF EXISTS shops'

    @staticmethod
    def create_shops():
        return ('CREATE TABLE shops('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'name varchar(100),'
                'email varchar(100) NULL,'
                'web_site varchar(200) NULL,'
                'phone_number varchar(20) NULL'
                ');')

    @staticmethod
    def create_btree_index():
        return 'CREATE INDEX shop_index ON shops(name, email, web_site, phone_number) USING  BTREE;'
