from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.genre import Genre

class GenreDAO(IDao):
    """A class for managing genres in the database."""

    def __init__(self, database: DatabaseConnection):
        """
         Initializes a GenreDAO instance.

         Parameters:
             database (DatabaseConnection): The database connection object.
         """
        super().__init__(database)

    def create(self, record: Genre):
        """
        Creates a new genre record in the database.

        Parameters:
            record (Genre): The genre record to be created.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            msg = "Error with creating genre."
            query = """
                    INSERT INTO genre(Name) VALUES(?)
                    """
            params = (record.name, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Retrieves genre records from the database.

        Returns:
            list: A list of genre names.

        Raises:
            Exception: If no records are found or an error occurs during the retrieval process.
        """
        msg = "No records."
        try:
            query = """
                    SELECT Name FROM genre
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record: Genre):
        """
        Updates an existing genre record in the database.

        Parameters:
            record (Genre): The genre record to be updated.

        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            msg = "Error with updating genre."
            query = """
                    UPDATE genre SET Name = ? WHERE ID = ?
                    """
            params = (record.name, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Genre):
        """
        Deletes a genre record from the database.

        Parameters:
            record (Genre): The genre record to be deleted.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        try:
            msg = "Error with deleting genre."
            query = """
                    DELETE FROM genre WHERE Name = ?
                    """
            params = (record.name,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)