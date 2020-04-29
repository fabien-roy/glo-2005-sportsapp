class MySQLEquipmentQuery:

    @staticmethod
    def drop_equipments():
        return 'DROP TABLE IF EXISTS equipments'

    @staticmethod
    def create_equipments():
        return ('CREATE TABLE equipments('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'manufacturer_id int NOT NULL,'
                'category_id int not NULL,'
                'name varchar(100),'
                'description varchar(1000),'
                'FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE,'
                'FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE'
                ');')
