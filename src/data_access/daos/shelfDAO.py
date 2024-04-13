from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.shelf import Shelf
from src.data_access.tables.book import Book


class ShelfDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: Shelf):
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
        msg = "No records."
        try:
            query = """
                    SELECT * FROM shelf
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record: Shelf):
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
        try:
            msg = "Error with creating record."
            query = """
                    EXEC Add_book_to_shelf ?,?,?;
                    """
            params = (book.title, record.shelf_no, record.floor,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)
