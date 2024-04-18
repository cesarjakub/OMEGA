from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.author import Author

class AuthorDAO(IDao):
    """A class for handling CRUD operations related to the Author table in the database."""

    def __init__(self, database: DatabaseConnection):
        """
        Initializes an AuthorDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def create(self, record: Author):
        """
        Creates a new author record in the database.

        Parameters:
            record (Author): The author record to be created.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            msg = "Error with creating admin."
            query = """
                    INSERT INTO author(First_name, Last_name) VALUES(?,?)
                    """
            params = (record.first_name, record.last_name, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Retrieves all author records from the database.

        Returns:
            list: A list of author records.

        Raises:
            Exception: If no records are found or an error occurs during the retrieval process.
        """
        msg = "No records."
        try:
            query = """
                    SELECT * FROM Books_author_genre
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record: Author):
        """
        Updates an existing author record in the database.

        Parameters:
            record (Author): The author record to be updated.

        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            msg = "Error with updating admin."
            query = """
                    UPDATE author SET First_name = ?, Last_name = ? WHERE ID = ?
                    """
            params = (record.first_name, record.last_name, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Author):
        """
        Deletes an author record from the database.

        Parameters:
            record (Author): The author record to be deleted.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        try:
            msg = "Error with deleting admin."
            query = """
                    DELETE FROM author WHERE First_name = ? and Last_name = ?
                    """
            params = (record.first_name, record.last_name,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_records(self):
        """
        Retrieves all first names of author records from the database.

        Returns:
            list: A list of first names of authors.

        Raises:
            Exception: If no records are found or an error occurs during the retrieval process.
        """
        msg = "No records."
        try:
            query = """
                    SELECT First_name FROM author;
                    """
            first_name_history = self.database.select(query, msg)
            return first_name_history
        except Exception as e:
            return msg

    def read_records_two(self):
        """
        Retrieves all last names of author records from the database.

        Returns:
            list: A list of last names of authors.

        Raises:
            Exception: If no records are found or an error occurs during the retrieval process.
        """
        msg = "No records."
        try:
            query = """
                    SELECT Last_name FROM author;
                    """
            last_name_history = self.database.select(query, msg)
            return last_name_history
        except Exception as e:
            return msg