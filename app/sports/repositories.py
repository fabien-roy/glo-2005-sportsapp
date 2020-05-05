from abc import ABCMeta, abstractmethod


class SportRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self, form=None, offset=None, per_page=None):
        """ abstract method """

    @abstractmethod
    def get_count(self, form=None):
        """ abstract method """

    @abstractmethod
    def get_all_for_equipment_type(self, type_id):
        """ abstract method """

    @abstractmethod
    def get(self, sport_id):
        """ abstract method """

    @abstractmethod
    def add(self, sport):
        """ abstract method """
