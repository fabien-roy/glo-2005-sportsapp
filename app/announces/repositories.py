from abc import ABCMeta, abstractmethod


class AnnounceRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all_for_shop(self, shop_id):
        """ abstract method """

    @abstractmethod
    def get_all_for_equipment(self, equipment_id):
        """ abstract method """

    @abstractmethod
    def add(self, announce, shop_id, equipment_id):
        """ abstract method """
