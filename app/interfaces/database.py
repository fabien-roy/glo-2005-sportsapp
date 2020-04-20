from abc import ABCMeta, abstractmethod


class Database:
    __metaclass__ = ABCMeta

    connection = None

    @abstractmethod
    def create_connection(self):
        """ abstract method """

    def connect(self):
        if self.connection is None:
            self.connection = self.create_connection()

        return self.connection
