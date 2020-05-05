from abc import abstractmethod, ABCMeta


class EquipmentRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self, form, offset, per_page):
        """ abstract method """

    @abstractmethod
    def get_count(self, form):
        """ abstract method """

    @abstractmethod
    def get(self, equipment_id):
        """ abstract method """

    @abstractmethod
    def get_by_name(self, param):
        """ abstract method """

    @abstractmethod
    def add(self, equipment):
        """ abstract method """
