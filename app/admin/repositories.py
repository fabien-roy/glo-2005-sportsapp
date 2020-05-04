from abc import abstractmethod, ABCMeta


class StatEventRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self):
        """ abstract method """

    @abstractmethod
    def add(self, event):
        """ abstract method """
