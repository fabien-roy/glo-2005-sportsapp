from injector import Module

from app.users.infrastructure.repositories import MySQLUserRepository
from app.users.repositories import UserRepository


class UserModule(Module):
    def configure(self, binder):
        binder.bind(UserRepository, to=MySQLUserRepository)
