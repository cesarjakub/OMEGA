from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.shelf import Shelf
from src.data_access.tables.book import Book


class ShelfDAO(IDao):
    """Data Access Object for interacting with shelf data in the database."""

    def __init__(self, database: DatabaseConnection):
        """
        Initializes a ShelfDAO instance.

        Parameters:
            database (DatabaseConnection): The database connection object.
        """
        super().__init__(database)

    def create(self, record: Shelf):
        """
        Creates a new shelf record in the database.

        Parameters:
            record (Shelf): The Shelf object containing the data to be inserted.

        Raises:
            Exception: If an error occurs while creating the shelf record.
        """
        try:
            msg = "Error with creating record."
            query = """
                    INSERT INTO shelf(Book_ID, Shelf_no, Floor)
                    VALUES (?,?,?)
                    """
            params = (record.book_id, record.shelf_no, record.floor,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        """
        Reads shelf records from the database.

        Returns:
            list: A list of shelf records.

        Raises:
            Exception: If an error occurs while reading the shelf records.
        """
        msg = "No records."
        try:
            query = """
                    SELECT * FROM Books_shelf
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record: Shelf):
        """
        Updates an existing shelf record in the database.

        Parameters:
            record (Shelf): The Shelf object containing the updated data.

        Raises:
            Exception: If an error occurs while updating the shelf record.
        """
        try:
            msg = "Error with updating record."
            query = """
                    UPDATE shelf
                    SET Book_ID = ?, Shelf_no = ?, Floor = ?
                    WHERE ID = ?;
                    """
            params = (record.book_id, record.shelf_no, record.floor, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Shelf):
        """
        Deletes a shelf record from the database.

        Parameters:
            record (Shelf): The Shelf object to be deleted.

        Raises:
            Exception: If an error occurs while deleting the shelf record.
        """
        try:
            msg = "Error with deleting record."
            query = """
                    DELETE FROM shelf WHERE ID = ?
                    """
            params = (record.id,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def insert_record(self, record: Shelf, book: Book):
        """
        Inserts a new shelf record with a specified book into the database.

        Parameters:
            record (Shelf): The Shelf object to be inserted.
            book (Book): The Book object to be associated with the shelf.

        Raises:
            Exception: If an error occurs while creating the shelf record.
        """
        try:
            msg = "Error with creating record."
            query = """
                    EXEC Add_book_to_shelf ?,?,?;
                    """
            params = (book.title, record.shelf_no, record.floor,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_record(self):
        """
        Reads shelf IDs from the database.

        Returns:
            list: A list of shelf IDs.

        Raises:
            Exception: If an error occurs while reading shelf IDs.
        """
        msg = "No records"
        try:
            query = """
                    SELECT ID FROM shelf
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg
