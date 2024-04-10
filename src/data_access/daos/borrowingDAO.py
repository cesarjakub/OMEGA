from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.borrowing import Borrowing
from src.data_access.tables.book import Book
from src.data_access.tables.users import Users

class BorrowingDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: Borrowing):
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
        try:
            msg = "No records."
            query = """
                    SELECT * FROM borrowing
                    """
            self.database.select(query, msg)
        except Exception as e:
            raise Exception(e)

    def update(self, record: Borrowing):
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
        try:
            msg = "Error with creating book copy."
            query = """
                    EXEC Create_borrowing_books ?,?,?,?,?;
                    """
            params = (book.title, users.first_name, users.last_name, record.date_borrowed, record.due_date, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)