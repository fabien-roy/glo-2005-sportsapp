from app.manufacturers.infrastructure.repositories import MySQLManufacturerRepository
from tests.interfaces.infrastructure.database import test_database
from tests.interfaces.infrastructure.test_repositories import RepositoryTests


class ManufacturerRepositoryTests(RepositoryTests):

    def setUp(self):
        super().setUp()
        self.repository = MySQLManufacturerRepository(test_database)
