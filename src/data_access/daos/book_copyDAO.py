from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.book_copy import BookCopy

class BookCopyDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record):
        pass

    def read(self):
        pass

    def update(self, record):
        pass

    def delete(self, record):
        pass