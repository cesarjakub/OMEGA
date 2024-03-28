from abc import ABC, abstractmethod
from src.data_access.database_connection import DatabaseConnection

class IDao(ABC):

    def __init__(self, database: DatabaseConnection):
        self.database = database

    @abstractmethod
    def create(self, record):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self, record):
        pass

    @abstractmethod
    def delete(self, record):
        pass