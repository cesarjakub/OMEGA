from src.data_access.daos.idao import IDao
from src.data_access.tables.book import Book

class BookDAO(IDao):

    def __init__(self):
        super().__init__()

    def create(self, record):
        pass

    def read(self):
        pass

    def update(self, record):
        pass

    def delete(self, record):
        pass