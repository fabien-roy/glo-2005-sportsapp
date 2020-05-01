from abc import abstractmethod, ABCMeta


class EquipmentTypeRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all_for_sport(self, sport_id):
        """ abstract method """

    @abstractmethod
    def add(self, equipment_type):
        """ abstract method """

    @abstractmethod
    def add_to_sport(self, equipment_type, sport):
        """ abstract method """
