from abc import abstractmethod, ABCMeta


class EquipmentRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self, form=None):
        """ abstract method """

    @abstractmethod
    def get(self, equipment_id):
        """ abstract method """

    @abstractmethod
    def add(self, equipment):
        """ abstract method """
