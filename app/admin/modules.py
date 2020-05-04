from injector import Module

from app.admin.infrastructure.repositories import MySQLStatEventRepository
from app.admin.repositories import StatEventRepository


class AdminModule(Module):
    def configure(self, binder):
        binder.bind(StatEventRepository, to=MySQLStatEventRepository)
