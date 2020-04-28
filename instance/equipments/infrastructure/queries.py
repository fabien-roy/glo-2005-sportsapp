class MySQLEquipmentQuery:

    @staticmethod
    def drop_equipments():
        return 'DROP TABLE IF EXISTS equipments'

    @staticmethod
    def create_equipments():
        return ('CREATE TABLE equipments('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'manufacturer_id int NOT NULL,'
                'category varchar(50),'
                'name varchar(100),'
                'description varchar(1000),'
                'FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE'
                ');')
