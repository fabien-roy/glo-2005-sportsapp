from abc import abstractmethod, ABCMeta


class EquipmentTypeRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, equipment_type):
        """ abstract method """
