from abc import abstractmethod, ABCMeta


class UserRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self, form):
        """ abstract method """

    @abstractmethod
    def get(self, username):
        """ abstract method """

    @abstractmethod
    def add(self, user):
        """ abstract method """
