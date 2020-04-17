from injector import Module

from instance import CreationService
from instance.creation.infrastructure.services import MySQLCreationService


class InstanceModule(Module):
    def configure(self, binder):
        binder.bind(CreationService, to=MySQLCreationService)
