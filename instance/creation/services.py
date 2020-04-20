from abc import abstractmethod, ABCMeta


class CreationService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def db_create(self):
        """ abstract method """
