from abc import ABC, abstractmethod
from src.data_access.database_connection import DatabaseConnection

class IDao(ABC):
    """An abstract base class defining the interface for Data Access Objects."""

    def __init__(self, database: DatabaseConnection):
        """
        Initializes an IDao instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        self.database = database

    @abstractmethod
    def create(self, record):
        """
        Abstract method for creating a record in the database.

        Parameters:
            record: The record to be created.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def read(self):
        """
        Abstract method for reading records from the database.

        Returns:
            The records retrieved from the database.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def update(self, record):
        """
        Abstract method for updating a record in the database.

        Parameters:
            record: The record to be updated.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def delete(self, record):
        """
        Abstract method for deleting a record from the database.

        Parameters:
            record: The record to be deleted.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass