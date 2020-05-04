from abc import ABCMeta, abstractmethod


class RecommendationRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all_for_sport(self, sport_id):
        """ abstract method """

    @abstractmethod
    def get_all_for_practice_center(self, practice_center_id):
        """ abstract method """

    @abstractmethod
    def get_all_for_sport_and_user(self, username):
        """ abstract method """

    @abstractmethod
    def get_all_for_practice_center_and_user(self, username):
        """ abstract method """

    @abstractmethod
    def add_to_sport(self, recommendation, sport_id):
        """ abstract method """

    @abstractmethod
    def add_to_practice_center(self, recommendation: object, practice_center_id: object) -> object:
        """ abstract method """
