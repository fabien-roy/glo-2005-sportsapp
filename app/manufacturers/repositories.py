from abc import abstractmethod, ABCMeta


class ManufacturerRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_by_name(self, name):
        """ abstract method """

    @abstractmethod
    def add(self, manufacturer):
        """ abstract method """
