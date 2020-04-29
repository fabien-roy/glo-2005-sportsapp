from abc import abstractmethod, ABCMeta


class CategoryRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, category):
        """ abstract method """
