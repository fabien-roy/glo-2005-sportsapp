from abc import abstractmethod, ABCMeta


class ClimateRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all_for_sport(self, sport_id):
        """ abstract method """

    @abstractmethod
    def get_all_for_practice_center(self, practice_center_id):
        """ abstract method """

    @abstractmethod
    def add(self, climate):
        """ abstract method """

    @abstractmethod
    def add_to_sport(self, climate, sport):
        """ abstract method """

    @abstractmethod
    def add_to_practice_center(self, climate, practice_center):
        """ abstract method """
