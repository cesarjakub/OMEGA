from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection

class CountDAO(IDao):
    """A class for counting records in the database."""

    def __int__(self, database: DatabaseConnection):
        """
        Initializes a CountDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def count_book(self):
        """
        Counts the number of books in the database.

        Returns:
            int: The count of books in the database.

        Raises:
            Exception: If an error occurs during the count process.
        """
        msg = "0"
        try:
            query = """
                    SELECT COUNT(*) FROM book;
                    """
            book_count = self.database.select(query, msg)
            return book_count
        except Exception as e:
            return msg

    def count_users(self):
        """
        Counts the number of users in the database.

        Returns:
            int: The count of users in the database.

        Raises:
            Exception: If an error occurs during the count process.
        """
        msg = "0"
        try:
            query = """
                    SELECT COUNT(*) FROM users;
                    """
            users_count = self.database.select(query, msg)
            return users_count
        except Exception as e:
            return msg

    def count_borrowing(self):
        """
        Counts the number of borrowing records in the database.

        Returns:
            int: The count of borrowing records in the database.

        Raises:
            Exception: If an error occurs during the count process.
        """
        msg = "0"
        try:
            query = """
                    SELECT COUNT(*) FROM borrowing;
                    """
            borrowing_count = self.database.select(query, msg)
            return borrowing_count
        except Exception as e:
            return msg

    def create(self, record):
        """
        Creates a new record in the database.

        Parameters:
            record: The record to be created.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            msg = "Error with creating book."
            query = """
                    INSERT INTO book(Genre_ID, Author_ID, Title) VALUES(?,?,?)
                    """
            params = (record.genre_id, record.author_id, record.title,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Retrieves records from the database.

        Returns:
            list: A list of records.

        Raises:
            Exception: If no records are found or an error occurs during the retrieval process.
        """
        msg = "No records."
        try:
            query = """
                            SELECT Title from book
                            """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record):
        """
        Updates an existing record in the database.

        Parameters:
            record: The record to be updated.

        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            msg = "Error with updating book."
            query = """
                    UPDATE book SET Genre_ID = ?, Author_ID = ?, Title = ? WHERE ID = ?
                    """
            params = (record.genre_id, record.author_id, record.title, record.id,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record):
        """
        Deletes a record from the database.

        Parameters:
            record: The record to be deleted.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        try:
            msg = "Error with deleting book."
            query = """
                    DELETE FROM book WHERE ID = ?
                    """
            params = (record.id,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)