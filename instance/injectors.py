from injector import Injector

from instance.modules import InstanceModule


class InstanceInjector:
    def __init__(self, modules):
        injector = Injector()

        for module in modules:
            injector.binder.install(module)

        injector.binder.install(InstanceModule)
