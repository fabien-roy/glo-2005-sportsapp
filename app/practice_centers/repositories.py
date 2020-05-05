from abc import abstractmethod, ABCMeta


class PracticeCenterRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self, form=None, offset=None, per_page=None):
        """ abstract method """

    @abstractmethod
    def get_count(self, form=None):
        """ abstract method """

    @abstractmethod
    def get(self, practice_center_id):
        """ abstract method """

    def get_by_name(self, param):
        pass

    @abstractmethod
    def add(self, practice_center):
        """ abstract method """
