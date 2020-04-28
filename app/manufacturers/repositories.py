from abc import abstractmethod, ABCMeta


class ManufacturerRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, manufacturer):
        """ abstract method """
