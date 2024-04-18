from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.book_copy import BookCopy
from src.data_access.tables.publisher import Publisher
from src.data_access.tables.book import Book


class BookCopyDAO(IDao):
    """A class for handling CRUD operations related to the BookCopy table in the database."""

    def __init__(self, database: DatabaseConnection):
        """
        Initializes a BookCopyDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def create(self, record: BookCopy):
        """
        Creates a new book copy record in the database.

        Parameters:
            record (BookCopy): The book copy record to be created.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            msg = "Error with creating book copy."
            query = """
                    INSERT INTO book_copy(Book_ID, Publisher_ID, Date_of_publication) 
                    VALUES (?, ?, GETDATE())
                    """
            params = (record.book_id, record.publisher_id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Retrieves all book copy records from the database.

        Raises:
            Exception: If no records are found or an error occurs during the retrieval process.
        """
        try:
            msg = "No records."
            query = """
                    SELECT * FROM book_copy
                    """
            self.database.select(query, msg)
        except Exception as e:
            raise Exception(e)

    def update(self, record: BookCopy):
        """
        Updates an existing book copy record in the database.

        Parameters:
            record (BookCopy): The book copy record to be updated.

        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            msg = "Error with updating book copy."
            query = """
                    UPDATE book_copy SET Book_ID = ?, Publisher_ID = ? WHERE ID = ?
                    """
            params = (record.book_id, record.publisher_id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: BookCopy):
        """
        Deletes a book copy record from the database.

        Parameters:
            record (BookCopy): The book copy record to be deleted.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        try:
            msg = "Error with deleting book copy."
            query = """
                    DELETE FROM book_copy WHERE ID = ?
                    """
            params = (record.id,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def insert_record(self, book: Book, publisher: Publisher):
        """
        Inserts a new book copy record into the database based on provided book and publisher information.

        Parameters:
            book (Book): The book information for the new record.
            publisher (Publisher): The publisher information for the new record.

        Raises:
            Exception: If an error occurs during the insertion process.
        """
        try:
            msg = "Error with creating book copy."
            query = """
                    EXEC Create_book_copy ?,?;
                    """
            params = (book.title, publisher.name,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)
