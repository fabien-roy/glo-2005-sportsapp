class MySQLAnnounceQuery:

    @staticmethod
    def drop_announces():
        return 'DROP TABLE IF EXISTS announces'

    @staticmethod
    def create_announces():
        return ('CREATE TABLE announces('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'shop_id int NOT NULL,'
                'equipment_id int NOT NULL,'
                'state varchar(100),'
                'price decimal,'
                'date timestamp,'
                'FOREIGN KEY (shop_id) REFERENCES shops(id) ON DELETE CASCADE,'
                'FOREIGN KEY (equipment_id) REFERENCES equipments(id) ON DELETE CASCADE'
                ');')
