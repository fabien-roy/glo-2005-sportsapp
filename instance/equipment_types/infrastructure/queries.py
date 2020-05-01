class MySQLEquipmentTypeQuery:

    @staticmethod
    def drop_categories():
        return 'DROP TABLE IF EXISTS equipment_types'

    @staticmethod
    def create_categories():
        return ('CREATE TABLE equipment_types('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'name varchar(100)'
                ');')
