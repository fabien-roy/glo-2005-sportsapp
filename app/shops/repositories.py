from abc import ABCMeta, abstractmethod


class ShopRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self, form=None, offset=None, per_page=None):
        """ abstract method """

    @abstractmethod
    def get_count(self, form=None):
        """ abstract method """

    @abstractmethod
    def get(self, shop_id):
        """ abstract method """

    @abstractmethod
    def add(self, shop):
        """ abstract method """
