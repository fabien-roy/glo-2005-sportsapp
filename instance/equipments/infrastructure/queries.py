class MySQLEquipmentQuery:

    @staticmethod
    def drop_equipments():
        return 'DROP TABLE IF EXISTS equipments'

    @staticmethod
    def create_equipments():
        return ('CREATE TABLE equipments('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'manufacturer_id int NOT NULL,'
                'type_id int not NULL,'
                'name varchar(100),'
                'description varchar(1000),'
                'FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE,'
                'FOREIGN KEY (type_id) REFERENCES equipment_types(id) ON DELETE CASCADE'
                ');')

    @staticmethod
    def create_btree_index():
        return 'CREATE INDEX equipment_index ON equipments(name) USING BTREE;'
