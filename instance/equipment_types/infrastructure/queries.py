class MySQLEquipmentTypeQuery:

    @staticmethod
    def drop_sport_equipment_types():
        return 'DROP TABLE IF EXISTS sport_equipment_types'

    @staticmethod
    def create_sport_equipment_types():
        return ('CREATE TABLE sport_equipment_types('
                'sport_id int NOT NULL,'
                'type_id int NOT NULL,'
                'PRIMARY KEY (sport_id, type_id),'
                'FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE,'
                'FOREIGN KEY (type_id) REFERENCES equipment_types(id) ON DELETE CASCADE'
                ');')

    @staticmethod
    def drop_equipment_types():
        return 'DROP TABLE IF EXISTS equipment_types'

    @staticmethod
    def create_equipment_types():
        return ('CREATE TABLE equipment_types('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'name varchar(100)'
                ');')

    @staticmethod
    def create_btree_index():
        return 'CREATE INDEX equipment_type_index ON equipment_types(name) USING BTREE;'
