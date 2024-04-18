from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection

class ImportDAO(IDao):
    """Data Access Object for importing data into the database."""

    def __int__(self, database: DatabaseConnection):
        """
        Initializes an ImportDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def import_data(self, Book_title, Author_first_name, Author_last_name, Genre_name, Publisher_name,
                    shelf_nu, floor_nu):
        """
        Imports data into the database.

        Parameters:
            book_title (str): The title of the book to import.
            author_first_name (str): The first name of the author of the book.
            author_last_name (str): The last name of the author of the book.
            genre_name (str): The genre of the book.
            publisher_name (str): The publisher of the book.
            shelf_number (int): The shelf number where the book is located.
            floor_number (int): The floor number where the book is located.

        Raises:
            Exception: If an error occurs while importing the data.
        """
        try:
            msg = "Error while importing data."
            query = """
                    EXEC Import_data ?,?,?,?,?,?,?;
                    """
            params = (Book_title, Author_first_name, Author_last_name, Genre_name, Publisher_name, shelf_nu, floor_nu, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def create(self, record):
        """
        Abstract method implementation.
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
        Abstract method implementation.
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
        Abstract method implementation.
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
        Abstract method implementation.
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