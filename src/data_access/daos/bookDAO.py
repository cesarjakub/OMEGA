from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.book import Book
from src.data_access.tables.genre import Genre
from src.data_access.tables.author import Author

class BookDAO(IDao):
    """A class for handling CRUD operations related to the Book table in the database."""

    def __init__(self, database: DatabaseConnection):
        """
        Initializes a BookDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def create(self, record: Book):
        """
        Creates a new book record in the database.

        Parameters:
            record (Book): The book record to be created.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            msg = "Error with creating book."
            query = """
                    INSERT INTO book(Genre_ID, Author_ID, Title) VALUES(?,?,?)
                    """
            params = (record.genre_id, record.author_id, record.title, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Retrieves all book titles from the database.

        Returns:
            list: A list of book titles.

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

    def update(self, record: Book):
        """
        Updates an existing book record in the database.

        Parameters:
            record (Book): The book record to be updated.

        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            msg = "Error with updating book."
            query = """
                    UPDATE book SET Genre_ID = ?, Author_ID = ?, Title = ? WHERE ID = ?
                    """
            params = (record.genre_id, record.author_id, record.title, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Book):
        """
        Deletes a book record from the database.

        Parameters:
            record (Book): The book record to be deleted.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        try:
            msg = "Error with deleting book."
            query = """
                    DELETE FROM book WHERE ID = ?
                    """
            params = (record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def insert_record(self, book: Book, genre: Genre, author: Author):
        """
        Inserts a new book record into the database based on provided book, genre, and author information.

        Parameters:
            book (Book): The book information for the new record.
            genre (Genre): The genre information for the new record.
            author (Author): The author information for the new record.

        Raises:
            Exception: If an error occurs during the insertion process.
        """
        try:
            msg = "Error with creating book."
            query = """
                    EXEC Add_book ?,?,?,?;
                    """
            params = (genre.name, author.first_name, author.last_name, book.title, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_record(self, book: Book):
        """
        Retrieves information about a specific book from the database.

        Parameters:
            book (Book): The book record to be retrieved.

        Returns:
            list: A list containing information about the book.

        Raises:
            Exception: If an error occurs during the retrieval process.
        """
        try:
            msg = "Error with reading book."
            query = """
                    EXEC Find_book ?;
                    """
            params = (book.title, )
            books_info = self.database.select_with_params(query, params, msg)
            return books_info
        except Exception as e:
            raise Exception(e)