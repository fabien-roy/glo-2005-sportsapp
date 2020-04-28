from abc import abstractmethod, ABCMeta


class ManufacturerRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, equipment):
        """ abstract method """
