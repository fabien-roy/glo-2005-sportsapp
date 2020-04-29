from injector import inject

from app.categories.repositories import CategoryRepository
from app.categories.infrastructure.queries import MySQLCategoryQuery as Query
from app.interfaces.database import Database


class MySQLCategoryRepository(CategoryRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def add(self, category):
        try:
            with self.database.connect().cursor() as cur:
                query = Query().add()
                cur.execute(query, category.name)

                self.database.connect().commit()

                category.id = cur.lastrowid

        finally:
            cur.close()
