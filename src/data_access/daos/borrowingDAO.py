from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.borrowing import Borrowing
from src.data_access.tables.book import Book
from src.data_access.tables.users import Users

class BorrowingDAO(IDao):
    """A class for handling CRUD operations related to borrowing records in the database."""

    def __init__(self, database: DatabaseConnection):
        """
        Initializes a BorrowingDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def create(self, record: Borrowing):
        """
        Creates a new borrowing record in the database.

        Parameters:
            record (Borrowing): The borrowing record to be created.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            msg = "Error with creating record."
            query = """
                    INSERT INTO borrowing (Book_ID, Users_ID, Borrowed_date, Due_date)
                    VALUES (?, ?, ?, ?);
                    """
            params = ()
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Retrieves all borrowing records from the database.

        Returns:
            list: A list of borrowing records.

        Raises:
            Exception: If no records are found or an error occurs during the retrieval process.
        """
        msg = "No records."
        try:
            query = """
                    SELECT * FROM Borrowed_books_by_users
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record: Borrowing):
        """
        Updates an existing borrowing record in the database.

        Parameters:
            record (Borrowing): The borrowing record to be updated.

        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            msg = "Error with updating record."
            query = """
                    UPDATE borrowing
                    SET Book_ID = ?, Users_ID = ?, Borrowed_date = ?, Due_date = ?
                    WHERE ID = ?;
                    """
            params = (record.book_id, record.users_id, record.date_borrowed, record.due_date, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Borrowing):
        """
        Deletes a borrowing record from the database.

        Parameters:
            record (Borrowing): The borrowing record to be deleted.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        try:
            msg = "Error with deleting record."
            query = """
                    DELETE FROM borrowing WHERE ID = ?
                    """
            params = (record.id,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def insert_record(self, record: Borrowing, book: Book, users: Users):
        """
        Inserts a new borrowing record into the database based on provided borrowing, book, and user information.

        Parameters:
            record (Borrowing): The borrowing information for the new record.
            book (Book): The book information for the new record.
            users (Users): The user information for the new record.

        Raises:
            Exception: If an error occurs during the insertion process.
        """
        try:
            msg = "Error with creating borrowing."
            query = """
                    EXEC Create_borrowing_books ?,?,?,?,?;
                    """
            params = (book.title, users.first_name, users.last_name, record.date_borrowed, record.due_date, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_record(self,):
        """
        Retrieves all borrowing IDs from the database.

        Returns:
            list: A list of borrowing IDs.

        Raises:
            Exception: If no records are found or an error occurs during the retrieval process.
        """
        msg = "No records"
        try:
            query = """
                    SELECT ID FROM borrowing
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg