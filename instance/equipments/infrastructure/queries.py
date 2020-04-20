class MySQLEquipmentQuery:

    @staticmethod
    def drop_equipments():
        return 'DROP TABLE IF EXISTS equipments'

    @staticmethod
    def create_equipments():
        return ('CREATE TABLE equipments('
                'id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                'category varchar(50),'
                'name varchar(100),'
                'description varchar(1000)'
                ');')
