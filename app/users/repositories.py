from abc import abstractmethod, ABCMeta


class UserRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all(self, form, offset, per_page):
        """ abstract method """

    @abstractmethod
    def get_count(self, form):
        """ abstract method """

    @abstractmethod
    def get(self, username):
        """ abstract method """

    @abstractmethod
    def get_touch(self, username):
        """ abstract method """

    @abstractmethod
    def add(self, user):
        """ abstract method """

    @abstractmethod
    def add_password(self, user):
        """ abstract method """

    @abstractmethod
    def get_password(self, username):
        """ abstract method """
