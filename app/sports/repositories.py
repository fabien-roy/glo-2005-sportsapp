from abc import ABCMeta, abstractmethod


class SportRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self, form=None):
        """ abstract method """

    @abstractmethod
    def get(self, sport_id):
        """ abstract method """

    @abstractmethod
    def add(self, sport):
        """ abstract method """
