from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.publisher import Publisher

class PublisherDAO(IDao):
    """Data Access Object for interacting with publisher data in the database."""

    def __init__(self, database: DatabaseConnection):
        """
        Initializes a PublisherDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def create(self, record: Publisher):
        """
        Creates a new publisher record in the database.

        Parameters:
            record (Publisher): The Publisher object containing the data to be inserted.

        Raises:
            Exception: If an error occurs while creating the publisher record.
        """
        try:
            msg = "Error with creating publisher."
            query = """
                    INSERT INTO publisher(Name) VALUES(?)
                    """
            params = (record.name, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Reads publisher records from the database.

        Returns:
            list: A list of publisher records.

        Raises:
            Exception: If an error occurs while reading the publisher records.
        """
        msg = "No records."
        try:
            query = """
                    SELECT * FROM Books_and_publisher
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record: Publisher):
        """
        Updates an existing publisher record in the database.

        Parameters:
            record (Publisher): The Publisher object containing the updated data.

        Raises:
            Exception: If an error occurs while updating the publisher record.
        """
        try:
            msg = "Error with updating publisher."
            query = """
                    UPDATE publisher SET Name = ? WHERE ID = ?
                    """
            params = (record.name, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Publisher):
        """
        Deletes a publisher record from the database.

        Parameters:
            record (Publisher): The Publisher object to be deleted.

        Raises:
            Exception: If an error occurs while deleting the publisher record.
        """
        try:
            msg = "Error with deleting publisher."
            query = """
                    DELETE FROM publisher WHERE Name = ?
                    """
            params = (record.name, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_records(self):
        """
        Reads publisher names from the database.

        Returns:
            list: A list of publisher names.

        Raises:
            Exception: If an error occurs while reading publisher names.
        """
        msg = "No records."
        try:
            query = """
                    SELECT Name FROM publisher
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg